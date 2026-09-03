#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
palanca.py - Apaga, aparta y anota. Todo reversible. Nunca borra.

    python3 .claude/skills/mantenimiento/scripts/palanca.py estado
    python3 .claude/skills/mantenimiento/scripts/palanca.py apagar <skill> --modo solo-usuario
    python3 .claude/skills/mantenimiento/scripts/palanca.py encender <skill>
    python3 .claude/skills/mantenimiento/scripts/palanca.py cuarentena <skill>
    python3 .claude/skills/mantenimiento/scripts/palanca.py restaurar <skill>
    python3 .claude/skills/mantenimiento/scripts/palanca.py bitacora "que fallo, cuando"

Cada cambio imprime su comando de reversa y respalda el settings.json que toca.
"""
import argparse
import datetime
import json
import os
import shutil
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
SETTINGS = os.path.join(RAIZ, ".claude", "settings.json")
SKILLS = os.path.join(RAIZ, ".claude", "skills")
CUARENTENA = os.path.join(RAIZ, ".claude", "cuarentena")
RESPALDOS = os.path.join(RAIZ, ".claude", "respaldos")
BITACORA = os.path.join(RAIZ, "BITACORA.md")
YO = ".claude/skills/mantenimiento/scripts/palanca.py"

MODOS = {"off": "off", "solo-nombre": "name-only", "solo-usuario": "user-invocable-only"}
EXPLICA = {
    "off": "no la ve nadie: ni el modelo ni tu",
    "name-only": "se lista sin descripcion: casi nunca se dispara sola, tu puedes invocarla",
    "user-invocable-only": "el modelo no la ve; tu la llamas con /<nombre>",
}
INVERSO = dict((v, k) for k, v in MODOS.items())


def carga(p):
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except OSError:
        return {}
    except ValueError as e:
        print("El settings.json esta roto (%s). Arreglalo antes de tocarlo." % e)
        sys.exit(2)


def respalda(p):
    if not os.path.isfile(p):
        return None
    os.makedirs(RESPALDOS, exist_ok=True)
    sello = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    destino = os.path.join(RESPALDOS, "settings.json." + sello)
    n = 1
    while os.path.exists(destino):          # nunca pisar un respaldo previo
        destino = os.path.join(RESPALDOS, "settings.json.%s-%d" % (sello, n))
        n += 1
    shutil.copy2(p, destino)
    return destino


def escribe(p, d):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def instaladas():
    if not os.path.isdir(SKILLS):
        return []
    return sorted(x for x in os.listdir(SKILLS)
                  if os.path.isfile(os.path.join(SKILLS, x, "SKILL.md")))


def apartadas():
    if not os.path.isdir(CUARENTENA):
        return []
    return sorted(x for x in os.listdir(CUARENTENA)
                  if os.path.isdir(os.path.join(CUARENTENA, x)))


def anota(linea):
    hoy = str(datetime.date.today())
    cabecera = "## %s — mantenimiento" % hoy
    previo = ""
    if os.path.isfile(BITACORA):
        with open(BITACORA, "r", encoding="utf-8") as f:
            previo = f.read()
    if cabecera in previo:
        partes = previo.split(cabecera, 1)
        nuevo = (partes[0] + cabecera + "\n\n- " + linea + "\n"
                 + partes[1].lstrip("\n"))
    else:
        entrada = "%s\n\n- %s\n\n" % (cabecera, linea)
        if previo.startswith("# "):
            corte = previo.find("\n\n")
            corte = len(previo) if corte == -1 else corte + 2
            nuevo = previo[:corte] + entrada + previo[corte:]
        else:
            nuevo = ("# Bitácora\n\n" if not previo else "") + entrada + previo
    with open(BITACORA, "w", encoding="utf-8") as f:
        f.write(nuevo)


# ------------------------------------------------------------------ comandos

def cmd_estado(_):
    d = carga(SETTINGS)
    ov = d.get("skillOverrides") or {}
    print("Skills de este workspace (%d): %s"
          % (len(instaladas()), ", ".join(instaladas()) or "ninguna"))
    if ov:
        print("\nApagadas o limitadas:")
        for k, v in sorted(ov.items()):
            print("  %-22s %-20s  (%s)" % (k, v, EXPLICA.get(v, "?")))
            print("      volver a encender:  python3 %s encender %s" % (YO, k))
    else:
        print("\nNinguna apagada ni limitada.")
    ap = apartadas()
    if ap:
        print("\nEn cuarentena (fuera de .claude/skills/, no se cargan):")
        for k in ap:
            print("  %-22s  restaurar:  python3 %s restaurar %s" % (k, YO, k))
    else:
        print("Nada en cuarentena.")
    print("\nA/B gratis y sin tocar nada:  claude --safe-mode")
    return 0


def cmd_apagar(a):
    modo = MODOS.get(a.modo)
    if not modo:
        print("Modo invalido. Usa: %s" % ", ".join(MODOS))
        return 1
    if a.skill not in instaladas():
        print("Aviso: '%s' no esta en .claude/skills/. Si es de tu carpeta personal o de un "
              "plugin, el override igual aplica." % a.skill)
    d = carga(SETTINGS)
    ov = d.setdefault("skillOverrides", {})
    antes = ov.get(a.skill)
    ov[a.skill] = modo
    copia = respalda(SETTINGS)
    escribe(SETTINGS, d)
    print("'%s' -> %s  (%s)" % (a.skill, modo, EXPLICA[modo]))
    if copia:
        print("Respaldo: %s" % os.path.relpath(copia, RAIZ))
    if antes:
        print("Deshacer: python3 %s apagar %s --modo %s"
              % (YO, a.skill, INVERSO.get(antes, "off")))
    else:
        print("Deshacer: python3 %s encender %s" % (YO, a.skill))
    anota("Apagada `%s` en modo %s. Razon: %s" % (a.skill, modo, a.razon or "sin anotar"))
    print("Anotado en BITACORA.md.")
    return 0


def cmd_encender(a):
    d = carga(SETTINGS)
    ov = d.get("skillOverrides") or {}
    if a.skill not in ov:
        print("'%s' no estaba apagada. Nada que hacer." % a.skill)
        return 0
    antes = ov.pop(a.skill)
    if not ov:
        d.pop("skillOverrides", None)
    copia = respalda(SETTINGS)
    escribe(SETTINGS, d)
    print("'%s' encendida (estaba en %s)." % (a.skill, antes))
    if copia:
        print("Respaldo: %s" % os.path.relpath(copia, RAIZ))
    print("Deshacer: python3 %s apagar %s --modo %s" % (YO, a.skill, INVERSO.get(antes, "off")))
    anota("Encendida de nuevo `%s`. Razon: %s" % (a.skill, a.razon or "sin anotar"))
    return 0


def cmd_cuarentena(a):
    origen = os.path.join(SKILLS, a.skill)
    if not os.path.isdir(origen):
        print("No existe la skill '%s' en este workspace." % a.skill)
        return 1
    os.makedirs(CUARENTENA, exist_ok=True)
    destino = os.path.join(CUARENTENA, a.skill)
    if os.path.exists(destino):
        print("Ya hay algo en cuarentena con ese nombre: %s" % os.path.relpath(destino, RAIZ))
        return 1
    shutil.move(origen, destino)
    print("'%s' apartada. No se borro nada: esta en %s"
          % (a.skill, os.path.relpath(destino, RAIZ)))
    print("Deshacer: python3 %s restaurar %s" % (YO, a.skill))
    anota("En cuarentena `%s`. Razon: %s" % (a.skill, a.razon or "sin anotar"))
    print("Anotado en BITACORA.md.")
    return 0


def cmd_restaurar(a):
    origen = os.path.join(CUARENTENA, a.skill)
    if not os.path.isdir(origen):
        print("'%s' no esta en cuarentena." % a.skill)
        return 1
    destino = os.path.join(SKILLS, a.skill)
    if os.path.exists(destino):
        print("Ya existe .claude/skills/%s. No lo piso." % a.skill)
        return 1
    shutil.move(origen, destino)
    print("'%s' restaurada en .claude/skills/." % a.skill)
    print("Deshacer: python3 %s cuarentena %s" % (YO, a.skill))
    anota("Restaurada `%s`. Razon: %s" % (a.skill, a.razon or "sin anotar"))
    return 0


def cmd_bitacora(a):
    anota(a.texto)
    print("Anotado en BITACORA.md: %s" % a.texto)
    return 0


def main():
    p = argparse.ArgumentParser(description="Palancas reversibles del workspace.")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("estado").set_defaults(fn=cmd_estado)

    ap = sub.add_parser("apagar")
    ap.add_argument("skill")
    ap.add_argument("--modo", default="solo-usuario", choices=list(MODOS))
    ap.add_argument("--razon", default="")
    ap.set_defaults(fn=cmd_apagar)

    en = sub.add_parser("encender")
    en.add_argument("skill")
    en.add_argument("--razon", default="")
    en.set_defaults(fn=cmd_encender)

    cu = sub.add_parser("cuarentena")
    cu.add_argument("skill")
    cu.add_argument("--razon", default="")
    cu.set_defaults(fn=cmd_cuarentena)

    re_ = sub.add_parser("restaurar")
    re_.add_argument("skill")
    re_.add_argument("--razon", default="")
    re_.set_defaults(fn=cmd_restaurar)

    bi = sub.add_parser("bitacora")
    bi.add_argument("texto")
    bi.set_defaults(fn=cmd_bitacora)

    a = p.parse_args()
    if not getattr(a, "fn", None):
        p.print_help()
        return 0
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
