#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nueva-skill.py - Andamiaje y control de calidad de las skills de este workspace.

    python3 .claude/skills/crear-skill/scripts/nueva-skill.py crear <nombre> [--referencias]
    python3 .claude/skills/crear-skill/scripts/nueva-skill.py verificar [nombre]
    python3 .claude/skills/crear-skill/scripts/nueva-skill.py listar

'verificar' es el espejo: sale 0 si la skill esta entregable, 1 si no.
No borra ni sobrescribe nada.
"""
import argparse
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
SKILLS = os.path.join(RAIZ, ".claude", "skills")
DESC_AVISO, DESC_TOPE = 500, 900
CUERPO_TOPE = 3000

ESQUELETO = """---
name: {n}
description: <Que hace, en una frase>. Usala cuando <situacion concreta>. Gatillos: <las palabras que esta persona usaria de verdad al pedirlo>.
---

# {t}

<Una linea: para que existe y que resultado deja.>

## Que hace

<El objetivo, no el procedimiento. Dos o tres frases.>

## El dato que el modelo no puede adivinar

<El formato exacto, el tono con ejemplos reales, la regla del negocio, la norma con su
version y su fecha. Si esta seccion queda vacia, no hagas la skill: haz un prompt.>

## Guardarrailes

- <Lo que no se toca.>
- <Lo que no se inventa, y de donde tiene que salir cada dato.>
- <Contra que se compara el resultado.>

## Criterio de termino

Listo cuando <condicion observable que se puede comprobar sin preguntarle a nadie>.
"""


def texto(p, limite=300000):
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read(limite)
    except OSError:
        return ""


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


def sin_codigo(t):
    """Quita bloques cercados y codigo en linea: ahi los <marcadores> son ejemplos, no errores."""
    t = re.sub(r"```.*?```", "", t, flags=re.DOTALL)
    t = re.sub(r"~~~.*?~~~", "", t, flags=re.DOTALL)
    t = re.sub(r"`[^`\n]*`", "", t)
    return t


def pasos(cuerpo):
    c = sin_codigo(cuerpo)
    n = len(re.findall(r"(?mi)^\s*(?:\d+[.)]\s|paso\s+\d|step\s+\d)", c))
    n += len(re.findall(r"(?mi)^\s*#+\s*(?:paso|step)\s*\d", c))
    return n


def existentes():
    if not os.path.isdir(SKILLS):
        return []
    return sorted(x for x in os.listdir(SKILLS)
                  if os.path.isfile(os.path.join(SKILLS, x, "SKILL.md")))


def cmd_crear(a):
    nombre = a.nombre.strip().lower()
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", nombre):
        print("El nombre va en kebab-case: solo minusculas, numeros y guiones.")
        print("  mal: 'Informe Mensual'   bien: 'informe-mensual'")
        return 1
    carpeta = os.path.join(SKILLS, nombre)
    destino = os.path.join(carpeta, "SKILL.md")
    if os.path.exists(destino):
        print("Ya existe %s. No lo sobrescribo." % os.path.relpath(destino, RAIZ))
        return 1
    os.makedirs(carpeta, exist_ok=True)
    titulo = nombre.replace("-", " ").capitalize()
    with open(destino, "w", encoding="utf-8") as f:
        f.write(ESQUELETO.format(n=nombre, t=titulo))
    if a.referencias:
        os.makedirs(os.path.join(carpeta, "references"), exist_ok=True)
    print("Creada: %s" % os.path.relpath(destino, RAIZ))
    print("Rellenala y despues:  python3 %s verificar %s"
          % (os.path.relpath(os.path.abspath(__file__), RAIZ), nombre))
    return 0


def revisa(nombre):
    """Devuelve (errores, avisos, datos) de una skill."""
    errores, avisos = [], []
    p = os.path.join(SKILLS, nombre, "SKILL.md")
    if not os.path.isfile(p):
        return (["%s: no existe SKILL.md, asi que Claude no la carga." % nombre], [], {})
    meta, cuerpo = frontmatter(texto(p))
    desc = meta.get("description", "")

    if not meta.get("name"):
        errores.append("%s: falta 'name' en el frontmatter." % nombre)
    elif meta["name"] != nombre:
        errores.append("%s: el frontmatter dice name '%s'; tiene que ser igual al nombre de la "
                       "carpeta." % (nombre, meta["name"]))
    if not desc:
        errores.append("%s: sin 'description'. Nunca se va a disparar sola." % nombre)
    elif len(desc) > DESC_TOPE:
        errores.append("%s: descripcion de %d caracteres (tope %d). Va a dispararse donde no "
                       "toca." % (nombre, len(desc), DESC_TOPE))
    elif len(desc) > DESC_AVISO:
        avisos.append("%s: descripcion de %d caracteres; por debajo de %d se dispara mejor."
                      % (nombre, len(desc), DESC_AVISO))
    if desc and "sala cuando" not in desc.lower() and "úsala" not in desc.lower() \
            and "usala" not in desc.lower() and "use " not in desc.lower():
        avisos.append("%s: la descripcion no dice CUANDO usarla. Agrega 'Usala cuando...'."
                      % nombre)
    if desc and not re.search(r"gatillo|trigger", desc, re.IGNORECASE):
        avisos.append("%s: sin palabras gatillo en la descripcion." % nombre)

    limpio = sin_codigo(cuerpo)
    marcas = re.findall(r"<[a-zA-Zñáéíóú][^>\n]{2,60}>", limpio)
    if marcas:
        errores.append("%s: quedaron marcadores de plantilla sin reemplazar (%d): %s"
                       % (nombre, len(marcas), marcas[0]))

    bajo = limpio.lower()
    if not re.search(r"^#+.*guardarra", cuerpo, re.MULTILINE | re.IGNORECASE):
        avisos.append("%s: no tiene seccion de guardarrailes." % nombre)
    if not re.search(r"^#+.*(criterio de t|listo cuando|done when)", cuerpo,
                     re.MULTILINE | re.IGNORECASE) and "listo cuando" not in bajo:
        errores.append("%s: no dice cuando termina. Sin criterio de termino, entrega algo que "
                       "parece listo y se va." % nombre)

    # Referencias rotas: una skill que apunta a un archivo que no existe falla en silencio.
    carpeta = os.path.join(SKILLS, nombre)
    # (?<![\w/.]) evita cortar una ruta larga a otra skill y creer que es propia.
    citadas = set(re.findall(
        r"(?<![\w/.])(?:references|scripts|plantillas|assets)/[A-Za-z0-9_.\-]+", cuerpo))
    rotas = [c for c in sorted(citadas) if not os.path.exists(os.path.join(carpeta, c))]
    if rotas:
        errores.append("%s: apunta a archivos que no existen: %s" % (nombre, ", ".join(rotas)))

    palabras = len(cuerpo.split())
    if palabras > CUERPO_TOPE:
        avisos.append("%s: cuerpo de %d palabras (tope comodo %d). Parte el detalle en "
                      "references/." % (nombre, palabras, CUERPO_TOPE))
    np = pasos(cuerpo)
    if np >= 12:
        avisos.append("%s: %d pasos numerados. Revisa si son limites o son manias: los pasos "
                      "envejecen con cada modelo." % (nombre, np))

    # Muletillas que el modelo ya trae. Se ignoran las lineas que las citan como
    # ejemplo de lo que NO hay que escribir (llevan comillas o una negacion delante).
    frases = ("se cuidadoso", "sé cuidadoso", "lee bien", "no inventes datos",
              "no inventes nada", "no te inventes", "piensa paso a paso",
              "asegurate de", "asegúrate de", "revisa bien", "ten cuidado")
    excusas = ("nada de", "no escribas", "en vez de", "muletilla", "evita ", "borra",
               '"', "\u201c", "\u00ab")
    ruido = []
    for linea in limpio.lower().splitlines():
        if any(x in linea for x in excusas):
            continue
        for f in frases:
            if f in linea and f not in ruido:
                ruido.append(f)
    if ruido:
        avisos.append("%s: contiene muletillas que el modelo ya trae (%s). Borralas."
                      % (nombre, ", ".join(ruido[:3])))

    return errores, avisos, {"desc": len(desc), "palabras": palabras, "pasos": np}


def cmd_verificar(a):
    objetivo = [a.nombre] if a.nombre else existentes()
    if not objetivo:
        print("No hay skills en .claude/skills/.")
        return 1
    errores, avisos = [], []
    for n in objetivo:
        e, av, _ = revisa(n)
        errores += e
        avisos += av
    ancho = 74
    print("=" * ancho)
    print("VERIFICACION DE SKILLS  ·  %s" % ", ".join(objetivo))
    print("=" * ancho)
    for x in avisos:
        print("  aviso %s" % x)
    for x in errores:
        print("  FALLA %s" % x)
    if not errores and not avisos:
        print("  Sin observaciones.")
    print("-" * ancho)
    if errores:
        print("FALLA — %d cosa(s) por arreglar." % len(errores))
        return 1
    print("PASA%s" % ("  (%d aviso[s], no bloquean)" % len(avisos) if avisos else ""))
    return 0


def cmd_listar(_):
    ns = existentes()
    if not ns:
        print("No hay skills en .claude/skills/.")
        return 0
    print("  %-22s %6s %8s %6s" % ("skill", "desc", "cuerpo", "pasos"))
    print("  " + "-" * 46)
    for n in ns:
        _, _, d = revisa(n)
        print("  %-22s %5dc %7dp %6d" % (n[:22], d.get("desc", 0), d.get("palabras", 0),
                                         d.get("pasos", 0)))
    print("\n  desc: caracteres que se leen en CADA sesion. cuerpo: solo al dispararse.")
    return 0


def main():
    p = argparse.ArgumentParser(description="Andamiaje y control de calidad de skills.")
    sub = p.add_subparsers(dest="cmd")
    c = sub.add_parser("crear")
    c.add_argument("nombre")
    c.add_argument("--referencias", action="store_true",
                   help="crea tambien la carpeta references/")
    c.set_defaults(fn=cmd_crear)
    v = sub.add_parser("verificar")
    v.add_argument("nombre", nargs="?")
    v.set_defaults(fn=cmd_verificar)
    sub.add_parser("listar").set_defaults(fn=cmd_listar)
    a = p.parse_args()
    if not getattr(a, "fn", None):
        p.print_help()
        return 0
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
