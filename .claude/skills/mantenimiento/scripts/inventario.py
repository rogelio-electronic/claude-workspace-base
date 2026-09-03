#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inventario.py - Mide el contexto que Claude Code carga de verdad en este workspace.

    python3 .claude/skills/mantenimiento/scripts/inventario.py [--json] [--todo]

Solo LEE. No modifica nada. Mira tamanos y frontmatter; no vuelca el contenido de tus archivos.
"""
import json
import os
import re
import sys
import time

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
HOME = os.path.expanduser("~")
CLAUDE_DIR = os.path.join(HOME, ".claude")
CHARS_POR_TOKEN = 4.0
IGNORAR = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".next"}


def tok(chars):
    return int(round(chars / CHARS_POR_TOKEN))


def leer(p, limite=400000):
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read(limite)
    except OSError:
        return ""


def dias(p):
    try:
        return int((time.time() - os.path.getmtime(p)) / 86400)
    except OSError:
        return -1


def rel(p):
    return p.replace(HOME, "~")


def corta(s, n):
    return s if len(s) <= n else "..." + s[-(n - 3):]


def frontmatter(t):
    if not t.startswith("---"):
        return {}, t
    fin = t.find("\n---", 3)
    if fin == -1:
        return {}, t
    crudo, cuerpo = t[3:fin], t[fin + 4:]
    meta, clave = {}, None
    for linea in crudo.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", linea)
        if m:
            clave = m.group(1).strip()
            meta[clave] = m.group(2).strip().strip('"').strip("'")
        elif clave and linea.strip():
            meta[clave] = (meta[clave] + " " + linea.strip()).strip()
    return meta, cuerpo


def pasos(cuerpo):
    c = re.sub(r"```.*?```", "", cuerpo, flags=re.DOTALL)
    n = len(re.findall(r"(?mi)^\s*(?:\d+[.)]\s|paso\s+\d|step\s+\d)", c))
    n += len(re.findall(r"(?mi)^\s*#+\s*(?:paso|step)\s*\d", c))
    return n


def cadena_claude_md():
    """Los CLAUDE.md que se cargan SIEMPRE al abrir sesion aqui: usuario + ancestros + este."""
    salida = []
    p = os.path.join(CLAUDE_DIR, "CLAUDE.md")
    if os.path.isfile(p):
        salida.append(("usuario", p))
    cadena, d = [], RAIZ
    while True:
        for nombre in ("CLAUDE.md", "CLAUDE.local.md"):
            q = os.path.join(d, nombre)
            if os.path.isfile(q):
                cadena.append(("workspace" if d == RAIZ else "carpeta-de-arriba", q))
        padre = os.path.dirname(d)
        if padre == d or len(d) <= len(HOME):
            break
        d = padre
    salida.extend(reversed(cadena))
    return salida


def raices_skills():
    r = [("workspace", os.path.join(RAIZ, ".claude", "skills")),
         ("personal", os.path.join(CLAUDE_DIR, "skills"))]
    cache = os.path.join(CLAUDE_DIR, "plugins", "cache")
    if os.path.isdir(cache):
        for dirpath, dirnames, _ in os.walk(cache):
            if os.path.basename(dirpath) == "skills":
                r.append(("plugin", dirpath))
                dirnames[:] = []
    return r


def analiza(p, origen):
    meta, cuerpo = frontmatter(leer(p))
    nombre = meta.get("name") or os.path.basename(os.path.dirname(p))
    desc = meta.get("description", "")
    return {
        "nombre": nombre, "origen": origen, "ruta": p,
        "desc_chars": len(desc),
        "siempre_tokens": tok(len(nombre) + len(desc) + 12),
        "cuerpo_palabras": len(cuerpo.split()),
        "pasos": pasos(cuerpo), "dias": dias(p),
        "sin_desc": not desc,
        "solo_usuario": str(meta.get("disable-model-invocation", "")).lower()
        in ("true", "1", "yes"),
    }


def huerfanas(cargadas):
    """SKILL.md dentro del workspace que Claude Code NO carga (fuera de .claude/skills)."""
    out = []
    for dirpath, dirnames, filenames in os.walk(RAIZ):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR]
        if "SKILL.md" in filenames:
            p = os.path.join(dirpath, "SKILL.md")
            if p not in cargadas:
                out.append(p)
    return out


def settings(p):
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def resto_del_arnes():
    fuentes = [("usuario", os.path.join(CLAUDE_DIR, "settings.json")),
               ("workspace", os.path.join(RAIZ, ".claude", "settings.json")),
               ("local", os.path.join(RAIZ, ".claude", "settings.local.json"))]
    hooks, overrides, mcp, plugins = [], {}, [], []
    for etiqueta, p in fuentes:
        if not os.path.isfile(p):
            continue
        d = settings(p)
        for evento, entradas in (d.get("hooks") or {}).items():
            n = sum(len(e.get("hooks", [])) for e in entradas) if isinstance(entradas, list) else 1
            hooks.append((etiqueta, evento, n))
        for k, v in (d.get("skillOverrides") or {}).items():
            overrides[k] = "%s (%s)" % (v, etiqueta)
        for k, v in (d.get("enabledPlugins") or {}).items():
            if v:
                plugins.append(k)
    for p in (os.path.join(CLAUDE_DIR, "mcp.json"), os.path.join(RAIZ, ".mcp.json")):
        if os.path.isfile(p):
            mcp.extend((settings(p).get("mcpServers") or {}).keys())
    return hooks, overrides, mcp, plugins


def main():
    flags = set(a for a in sys.argv[1:] if a.startswith("--"))
    todo = "--todo" in flags

    cadena = cadena_claude_md()
    md_chars = sum(os.path.getsize(p) for _, p in cadena)

    skills, cargadas = [], set()
    for etiqueta, raiz in raices_skills():
        if not os.path.isdir(raiz):
            continue
        for n in sorted(os.listdir(raiz)):
            sk = os.path.join(raiz, n, "SKILL.md")
            if os.path.isfile(sk):
                cargadas.add(sk)
                skills.append(analiza(sk, etiqueta))
    muertas = huerfanas(cargadas)
    hooks, overrides, mcp, plugins = resto_del_arnes()

    desc_tokens = sum(s["siempre_tokens"] for s in skills)
    total = tok(md_chars) + desc_tokens

    if "--json" in flags:
        print(json.dumps({
            "workspace": RAIZ,
            "claude_md": [{"tipo": t, "ruta": p, "tokens": tok(os.path.getsize(p))}
                          for t, p in cadena],
            "skills": skills, "skills_no_cargadas": muertas, "hooks": hooks,
            "skill_overrides": overrides, "mcp": mcp, "plugins": plugins,
            "tokens_siempre_activos": total,
        }, ensure_ascii=False, indent=2))
        return 0

    W = 78
    print("=" * W)
    print("INVENTARIO DE CONTEXTO  ·  %s" % os.path.basename(RAIZ))
    print("=" * W)

    print("\n1. SIEMPRE ACTIVO  (entra en cada sesion, escribas lo que escribas)")
    print("-" * W)
    if not cadena:
        print("   (sin CLAUDE.md)")
    for tipo, p in cadena:
        print("   %-17s %-44s ~%5d tok  %4dd"
              % (tipo, corta(rel(p), 44), tok(os.path.getsize(p)), dias(p)))
    print("   %-17s %-44s ~%5d tok"
          % ("skills", "%d descripciones (solo el frontmatter)" % len(skills), desc_tokens))
    print("   " + "-" * (W - 3))
    print("   TOTAL SIEMPRE ACTIVO: ~%d tokens" % total)

    print("\n2. SKILLS QUE SI SE CARGAN  (%d)" % len(skills))
    print("-" * W)
    print("   %-22s %-10s %6s %8s %6s %5s" % ("nombre", "origen", "desc", "cuerpo", "pasos", "dias"))
    for s in sorted(skills, key=lambda x: (-x["siempre_tokens"], x["nombre"])):
        marcas = []
        if s["sin_desc"]:
            marcas.append("SIN-DESC")
        if s["desc_chars"] > 500:
            marcas.append("desc-larga")
        if s["cuerpo_palabras"] > 3000:
            marcas.append("cuerpo-gordo")
        if s["pasos"] >= 12:
            marcas.append("micromanaging")
        if s["dias"] > 120:
            marcas.append("vieja")
        if s["nombre"] in overrides:
            marcas.append("override:%s" % overrides[s["nombre"]])
        if s["solo_usuario"]:
            marcas.append("solo-/nombre")
        print("   %-22s %-10s %5dc %7dp %6d %5d  %s"
              % (s["nombre"][:22], s["origen"], s["desc_chars"], s["cuerpo_palabras"],
                 s["pasos"], s["dias"], " ".join(marcas)))

    if muertas:
        print("\n3. SKILL.md EN DISCO QUE **NO** SE CARGAN  (%d)" % len(muertas))
        print("-" * W)
        print("   Estan fuera de .claude/skills/: hoy no cuestan contexto ni sesgan nada.")
        for p in (muertas if todo else muertas[:10]):
            print("   · %s" % corta(rel(p), 68))
        if not todo and len(muertas) > 10:
            print("   ... y %d mas (--todo para verlas)" % (len(muertas) - 10))

    print("\n4. RESTO DEL ARNES")
    print("-" * W)
    print("   hooks activos   : %s"
          % (", ".join("%s/%s x%d" % h for h in hooks) if hooks else "ninguno"))
    print("   plugins activos : %s" % (", ".join(plugins) if plugins else "ninguno"))
    print("   servidores MCP  : %s" % (", ".join(sorted(set(mcp))) if mcp else "ninguno"))
    print("   skillOverrides  : %s"
          % (", ".join("%s=%s" % (k, v) for k, v in overrides.items()) if overrides else "ninguno"))

    print("\n5. CANDIDATOS A REVISION")
    print("-" * W)
    cand = [s for s in skills if s["dias"] > 120 or s["pasos"] >= 12
            or s["desc_chars"] > 500 or s["sin_desc"]]
    if not cand:
        print("   Nada evidente. Igual pasales el filtro de las 3R a mano:")
        print("   repetible, requisito, repartible.")
    for s in sorted(cand, key=lambda x: -x["dias"]):
        razon = []
        if s["dias"] > 120:
            razon.append("%dd sin tocar" % s["dias"])
        if s["pasos"] >= 12:
            razon.append("%d pasos (hobbling)" % s["pasos"])
        if s["desc_chars"] > 500:
            razon.append("descripcion de %dc" % s["desc_chars"])
        if s["sin_desc"]:
            razon.append("sin descripcion: nunca se dispara sola")
        print("   · %-20s %s" % (s["nombre"][:20], "; ".join(razon)))

    print("\n   Siguiente:  python3 .claude/skills/mantenimiento/scripts/palanca.py estado")
    print("   A/B gratis: claude --safe-mode   (todo apagado, nada borrado)")
    print("\nNota: los tokens son estimacion (caracteres/4). Sirven para comparar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
