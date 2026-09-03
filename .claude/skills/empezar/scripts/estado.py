#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
estado.py - Memoria y verificacion de la configuracion del workspace.

    python3 .claude/skills/empezar/scripts/estado.py ver
    python3 .claude/skills/empezar/scripts/estado.py init --resumen "..." --perfil ... [mas]
    python3 .claude/skills/empezar/scripts/estado.py skill <nombre> [--via V] [--estado E]
    python3 .claude/skills/empezar/scripts/estado.py nota "texto"
    python3 .claude/skills/empezar/scripts/estado.py set <clave> <valor>
    python3 .claude/skills/empezar/scripts/estado.py verificar

'verificar' es el espejo: sale 0 si el workspace esta entregable, 1 si no.
"""
import argparse
import datetime
import json
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
ESTADO = os.path.join(RAIZ, ".claude", "estado.json")
SKILLS = os.path.join(RAIZ, ".claude", "skills")
VIAS = ("investigacion", "internet", "contexto", "pendiente")
LINEAS_AVISO, LINEAS_TOPE = 45, 80
DESC_AVISO, DESC_TOPE = 500, 900


def hoy():
    return datetime.date.today()


def mas_meses(fecha, meses):
    mes = fecha.month - 1 + meses
    anio = fecha.year + mes // 12
    mes = mes % 12 + 1
    dia = min(fecha.day, [31, 29 if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
                          else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mes - 1])
    return datetime.date(anio, mes, dia)


def leer():
    if not os.path.isfile(ESTADO):
        return None
    try:
        with open(ESTADO, "r", encoding="utf-8") as f:
            return json.load(f)
    except ValueError as e:
        print("estado.json existe pero esta roto: %s" % e)
        return None


def guardar(d):
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    with open(ESTADO, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")


def lista(valor):
    if not valor:
        return []
    return [x.strip() for x in valor.split(",") if x.strip()]


def texto(path, limite=200000):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read(limite)
    except OSError:
        return ""


def sin_codigo(t):
    """Quita bloques cercados y codigo en linea antes de buscar marcadores de plantilla."""
    t = re.sub(r"```.*?```", "", t, flags=re.DOTALL)
    t = re.sub(r"~~~.*?~~~", "", t, flags=re.DOTALL)
    t = re.sub(r"`[^`\n]*`", "", t)
    return t


def frontmatter(t):
    """Parser minimo de frontmatter YAML. Devuelve (dict, cuerpo)."""
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


# ---------------------------------------------------------------- comandos

def cmd_ver(_):
    d = leer()
    if not d or not d.get("configurado"):
        print("Workspace SIN CONFIGURAR.")
        print("Corre la skill `empezar` (o escribe: empezar).")
        return 0
    print("Workspace configurado el %s" % d.get("fecha_configuracion", "?"))
    print("  Resumen   : %s" % d.get("resumen", "-"))
    print("  Perfil    : %s   Idioma: %s   Nivel: %s   Estilo: %s"
          % (d.get("perfil", "-"), d.get("idioma", "-"),
             d.get("nivel_tecnico", "-"), d.get("estilo_respuesta", "-")))
    for etiqueta, clave in (("Trabajo   ", "trabajo"), ("Archivos  ", "archivos"),
                            ("Carpetas  ", "carpetas"), ("Limites   ", "limites")):
        if d.get(clave):
            print("  %s: %s" % (etiqueta, ", ".join(d[clave])))
    if d.get("compartido"):
        print("  Alcance   : %s" % d["compartido"])
    sk = d.get("skills") or []
    print("  Skills    : %s" % (", ".join("%s (%s/%s)" % (s.get("nombre"), s.get("via"),
                                                          s.get("estado"))
                                          for s in sk) if sk else "ninguna propia todavia"))
    for n in (d.get("notas") or []):
        print("  Nota      : %s" % n)
    print("  Proxima revision: %s" % d.get("proxima_revision", "-"))
    return 0


def cmd_init(a):
    previo = leer() or {}
    d = {
        "version": 1,
        "configurado": True,
        "fecha_configuracion": str(hoy()),
        "proxima_revision": a.revision or str(mas_meses(hoy(), 3)),
        "resumen": a.resumen,
        "perfil": a.perfil,
        "idioma": a.idioma,
        "nivel_tecnico": a.nivel,
        "estilo_respuesta": a.estilo,
        "trabajo": lista(a.trabajo),
        "archivos": lista(a.archivos),
        "limites": lista(a.limites),
        "compartido": a.compartido or "",
        "carpetas": lista(a.carpetas),
        "skills": previo.get("skills", []),
        "notas": previo.get("notas", []),
    }
    guardar(d)
    print("estado.json escrito. Proxima revision: %s" % d["proxima_revision"])
    return 0


def cmd_skill(a):
    d = leer()
    if not d:
        print("Todavia no hay estado.json. Corre 'init' primero.")
        return 1
    d.setdefault("skills", [])
    for s in d["skills"]:
        if s.get("nombre") == a.nombre:
            if a.via:
                s["via"] = a.via
            if a.estado:
                s["estado"] = a.estado
            guardar(d)
            print("Actualizada: %s (%s/%s)" % (s["nombre"], s.get("via"), s.get("estado")))
            return 0
    d["skills"].append({"nombre": a.nombre, "via": a.via or "pendiente",
                        "estado": a.estado or "pendiente", "fecha": str(hoy())})
    guardar(d)
    print("Anotada: %s (%s/%s)" % (a.nombre, a.via or "pendiente", a.estado or "pendiente"))
    return 0


def cmd_nota(a):
    d = leer()
    if not d:
        print("Todavia no hay estado.json. Corre 'init' primero.")
        return 1
    d.setdefault("notas", []).append(a.texto)
    guardar(d)
    print("Nota anotada.")
    return 0


def cmd_set(a):
    d = leer()
    if not d:
        print("Todavia no hay estado.json. Corre 'init' primero.")
        return 1
    valor = a.valor
    if "," in valor and a.clave in ("trabajo", "archivos", "limites", "carpetas"):
        valor = lista(valor)
    d[a.clave] = valor
    guardar(d)
    print("%s = %s" % (a.clave, valor))
    return 0


# ---------------------------------------------------------------- verificar

def cmd_verificar(_):
    errores, avisos, bien = [], [], []

    d = leer()
    if not d:
        errores.append("No existe .claude/estado.json (o esta roto). Corre 'init'.")
    elif not d.get("configurado"):
        errores.append("estado.json dice configurado=false.")
    else:
        faltan = [k for k in ("resumen", "perfil", "idioma", "proxima_revision")
                  if not d.get(k)]
        if faltan:
            errores.append("estado.json sin: %s" % ", ".join(faltan))
        else:
            bien.append("estado.json completo (perfil: %s)" % d.get("perfil"))
        try:
            datetime.datetime.strptime(d.get("proxima_revision", ""), "%Y-%m-%d")
            bien.append("proxima revision: %s" % d["proxima_revision"])
        except ValueError:
            errores.append("proxima_revision no es una fecha AAAA-MM-DD.")

    # --- CLAUDE.md
    cmd_path = os.path.join(RAIZ, "CLAUDE.md")
    if not os.path.isfile(cmd_path):
        errores.append("Falta CLAUDE.md en la raiz del workspace.")
    else:
        t = texto(cmd_path)
        n = len([l for l in t.splitlines() if l.strip()])
        if "todavía no está configurado" in t or "todavia no esta configurado" in t.lower():
            errores.append("CLAUDE.md sigue siendo la plantilla sin configurar.")
        limpio = sin_codigo(t)
        # OJO: 'TODO' solo en mayusculas. En espanol "todo" es una palabra normal.
        marcas = re.findall(r"<[a-zñáéíóú][^>\n]{2,40}>|\[completar\]|\{\{[^}]+\}\}",
                            limpio, re.IGNORECASE)
        marcas += re.findall(r"\bTODO\b|\bFIXME\b|\bPENDIENTE:\b", limpio)
        if marcas:
            errores.append("CLAUDE.md tiene marcadores sin reemplazar: %s"
                           % ", ".join(sorted(set(marcas))[:4]))
        if n > LINEAS_TOPE:
            errores.append("CLAUDE.md tiene %d lineas con texto (tope %d). Se lee en CADA "
                           "sesion: corta lo que no cambie una decision." % (n, LINEAS_TOPE))
        elif n > LINEAS_AVISO:
            avisos.append("CLAUDE.md tiene %d lineas (comodo: %d o menos)." % (n, LINEAS_AVISO))
        else:
            bien.append("CLAUDE.md: %d lineas, cabe en una pantalla" % n)

    # --- carpetas declaradas
    if d and d.get("carpetas"):
        faltan = [c for c in d["carpetas"] if not os.path.isdir(os.path.join(RAIZ, c))]
        if faltan:
            errores.append("Carpetas declaradas que no existen: %s" % ", ".join(faltan))
        else:
            bien.append("las %d carpetas declaradas existen" % len(d["carpetas"]))

    # --- skills
    if os.path.isdir(SKILLS):
        nombres = sorted(x for x in os.listdir(SKILLS)
                         if os.path.isdir(os.path.join(SKILLS, x)) and not x.startswith("."))
        for nombre in nombres:
            p = os.path.join(SKILLS, nombre, "SKILL.md")
            if not os.path.isfile(p):
                avisos.append("%s/ no tiene SKILL.md: no se carga." % nombre)
                continue
            meta, cuerpo = frontmatter(texto(p))
            if not meta.get("name"):
                errores.append("%s: SKILL.md sin 'name' en el frontmatter." % nombre)
            elif meta["name"] != nombre:
                errores.append("%s: el 'name' del frontmatter dice '%s'. Tienen que coincidir."
                               % (nombre, meta["name"]))
            desc = meta.get("description", "")
            if not desc:
                errores.append("%s: sin 'description'. Nunca se va a disparar sola." % nombre)
            elif len(desc) > DESC_TOPE:
                errores.append("%s: descripcion de %d caracteres (tope %d). Se dispara donde no "
                               "debe." % (nombre, len(desc), DESC_TOPE))
            elif len(desc) > DESC_AVISO:
                avisos.append("%s: descripcion de %d caracteres; %d es mas sano."
                              % (nombre, len(desc), DESC_AVISO))
            if len(cuerpo.split()) > 3000:
                avisos.append("%s: cuerpo de %d palabras. Parte el detalle en references/."
                              % (nombre, len(cuerpo.split())))
        if nombres:
            bien.append("%d skills revisadas: %s" % (len(nombres), ", ".join(nombres)))

    # --- bitacora
    bit = os.path.join(RAIZ, "BITACORA.md")
    if not os.path.isfile(bit):
        errores.append("Falta BITACORA.md con la entrada de hoy.")
    elif not re.search(r"^##\s+\d{4}-\d{2}-\d{2}", texto(bit), re.MULTILINE):
        errores.append("BITACORA.md no tiene ninguna entrada con fecha (## AAAA-MM-DD).")
    else:
        bien.append("BITACORA.md con entradas fechadas")

    # --- pendientes (informativo, no bloquea)
    pend = [s["nombre"] for s in ((d or {}).get("skills") or [])
            if s.get("estado") == "pendiente"]

    ancho = 74
    print("=" * ancho)
    print("VERIFICACION DEL WORKSPACE  ·  %s" % os.path.basename(RAIZ))
    print("=" * ancho)
    for b in bien:
        print("  OK    %s" % b)
    for a_ in avisos:
        print("  aviso %s" % a_)
    for e in errores:
        print("  FALLA %s" % e)
    if pend:
        print("  ---   pendientes anotados: %s" % ", ".join(pend))
    print("-" * ancho)
    if errores:
        print("FALLA — %d cosa(s) por arreglar antes de entregar esto." % len(errores))
        return 1
    print("PASA — el workspace esta entregable." +
          ("  (%d aviso[s], no bloquean)" % len(avisos) if avisos else ""))
    return 0


def main():
    p = argparse.ArgumentParser(description="Estado y verificacion del workspace.")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("ver").set_defaults(fn=cmd_ver)

    i = sub.add_parser("init")
    i.add_argument("--resumen", required=True)
    i.add_argument("--perfil", required=True)
    i.add_argument("--idioma", default="es")
    i.add_argument("--nivel", default="basico",
                   choices=["nuevo", "basico", "tecnico"])
    i.add_argument("--estilo", default="breve",
                   choices=["breve", "explicado", "tecnico"])
    i.add_argument("--trabajo", default="")
    i.add_argument("--archivos", default="")
    i.add_argument("--limites", default="")
    i.add_argument("--compartido", default="")
    i.add_argument("--carpetas", default="")
    i.add_argument("--revision", default="")
    i.set_defaults(fn=cmd_init)

    s = sub.add_parser("skill")
    s.add_argument("nombre")
    s.add_argument("--via", choices=list(VIAS))
    s.add_argument("--estado", choices=["pendiente", "investigando", "lista", "descartada"])
    s.set_defaults(fn=cmd_skill)

    n = sub.add_parser("nota")
    n.add_argument("texto")
    n.set_defaults(fn=cmd_nota)

    st = sub.add_parser("set")
    st.add_argument("clave")
    st.add_argument("valor")
    st.set_defaults(fn=cmd_set)

    sub.add_parser("verificar").set_defaults(fn=cmd_verificar)

    a = p.parse_args()
    if not getattr(a, "fn", None):
        p.print_help()
        return 0
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
