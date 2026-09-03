---
name: mantenimiento
description: Revisa qué configuración de este workspace se está cargando de verdad, mide cuánto contexto cuesta en cada sesión y apaga lo que sobra sin borrar nada. Úsala cuando pidan revisar, limpiar u ordenar el workspace, cuando algo se dispare donde no debe, cuando Claude responda raro o lento, cuando salga un modelo nuevo, o al llegar la fecha de revisión. Gatillos: revisar workspace, limpiar, sobra, va lento, se dispara sola, auditar skills, borrar una skill.
---

# Mantenimiento

Mantiene este workspace flaco. Mide lo que se carga de verdad, decide qué se queda con un criterio
escrito, y apaga lo demás de forma reversible.

La tesis: hoy el riesgo no es que a Claude le falte instrucción, es que le sobre. Una instrucción
escrita hace seis meses no se degrada sola — se queda ahí, apretando el caballo. Y el daño de una
skill vieja casi nunca es su tamaño: es que **se dispara donde no debía y te clava su camino**.

## Qué cuesta qué

| Qué | Cuándo entra | Costo real |
|---|---|---|
| `CLAUDE.md` (este y los de arriba) | siempre, completo | tokens en cada sesión: **aquí vive el impuesto** |
| Descripción de cada skill | siempre, una o dos líneas | pocos tokens, pero **decide qué se dispara** |
| Cuerpo de una skill | solo al dispararse | sesgo: te fija un camino aunque haya uno mejor |
| Hooks, MCP, plugins | siempre | tokens, latencia y superficie de fallo |

Por eso una descripción vaga hace más daño que una skill larga.

## Medir antes de opinar

```bash
python3 .claude/skills/mantenimiento/scripts/inventario.py          # --json  --todo
```

Trae números reales: qué se carga, qué está en disco pero no se carga (archivo muerto) y qué se
carga y además sesga. Si no lo midió el script, no lo afirmes.

Presenta el resultado como una tabla con **un veredicto por skill y su razón en una línea**.

## El filtro

Una skill se queda si pasa las tres R —**repetible** (la misma tarea, igual, tres o más veces al
mes), **requisito** (lleva dentro un dato que el modelo no puede adivinar) y **repartible** (otro la
correría igual)— y además sobrevive la prueba de hobbling: si le quitas los pasos y dejas solo el
dato duro, ¿pierdes algo? Si no pierdes nada, era andamio.

Detalle, tabla de veredictos y qué palanca corresponde a cada uno: `references/filtro-3r.md`.

## Apagar sin borrar

```bash
python3 .claude/skills/mantenimiento/scripts/palanca.py estado
python3 .claude/skills/mantenimiento/scripts/palanca.py apagar <skill> --modo solo-usuario
python3 .claude/skills/mantenimiento/scripts/palanca.py cuarentena <skill>
python3 .claude/skills/mantenimiento/scripts/palanca.py bitacora "qué falló, cuándo"
```

La prueba honesta de si algo hace falta es apagarlo y trabajar sin ello. Gratis y sin perder nada:
`claude --safe-mode` levanta una sesión con toda la personalización desactivada.

Y la mitad que casi nadie hace: **volver a subir línea por línea**. Solo regresa lo que falló dos
veces en uso real, y la bitácora dice por qué. Sin evidencia, no vuelve nada.

## Cuando lo que sobra es el `CLAUDE.md`

Es lo más caro y lo que más engorda. Tacha línea por línea con una sola pregunta: **¿Claude haría
algo distinto si esta línea no estuviera?** Si no, fuera. Los sospechosos habituales: recordatorios
de sentido común, resúmenes de lo que ya se ve en la carpeta, listas de skills que se desactualizan
solas, y procedimientos de doce pasos que querían ser una skill.

## Guardarraíles

- **Nunca borres.** Apagado o cuarentena, siempre con su comando de deshacer impreso. Quien borra
  es el usuario, no tú.
- **Números del script, no de tu cabeza.**
- **Un cambio por vez y avisado.** Si apagas tres cosas juntas y algo se rompe, no sabes cuál fue.
- **No edites skills de plugins en su sitio**: se pierden al actualizar. Cópialas a
  `.claude/skills/` y adapta ahí.
- **Auditar no obliga a cortar.** Si el usuario no aprueba un cambio, se queda como está y se anota.
- **Esta skill se somete a su propia regla.** Si te empuja a un plan de doce pasos para algo que se
  resuelve con una frase, ignórala y resuélvelo con la frase.

## Criterio de término

Listo cuando:

1. Cada skill que sí se carga tiene su veredicto —queda, reescribir, solo-nombre, solo-usuario,
   cuarentena— **con la razón en una línea**.
2. Todo cambio aplicado quedó impreso con su comando de reversa, y **nada se borró**.
3. `BITACORA.md` tiene la entrada de hoy con la próxima fecha de revisión.
4. Le dijiste al usuario el antes/después en tokens siempre activos y **qué va a notar distinto**.

## Referencias

- `references/filtro-3r.md` — el filtro completo, la prueba de hobbling y la tabla veredicto → palanca.
- `scripts/inventario.py` — qué se carga y cuánto cuesta.
- `scripts/palanca.py` — apagar, poner en cuarentena y anotar, todo reversible.

> Método de ablación de Rogelio Gómez. Si en esta máquina existe además la skill `ablacion` a nivel
> de usuario, esa es la versión completa: úsala a ella y deja esta para lo de este workspace.
