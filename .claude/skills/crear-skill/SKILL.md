---
name: crear-skill
description: Convierte una necesidad repetida en una skill de este workspace por tres vías: investigación profunda (Gemini, Perplexity), adaptar una que ya existe en internet, o el contexto del usuario. Trae el filtro que decide si algo merece ser skill o basta una línea en CLAUDE.md. Úsala al crear, agregar, buscar o mejorar una habilidad. Gatillos: crear skill, nueva skill, quiero que aprendas a, que siempre lo hagas así, buscar una skill.
---

# Crear skill

Convierte algo que esta persona hace una y otra vez en una habilidad que Claude ejecuta siempre
igual y a su manera. Y —esto es la mitad del trabajo— dice que no cuando lo que pidieron no
necesita una skill.

## Primero el filtro, siempre

Una skill se queda cargada para siempre y sesga todas las sesiones donde se dispara. Por eso se
gana el puesto, no se regala. Hazle las tres preguntas antes de escribir una sola línea:

1. **¿Repetible?** ¿Hace esa tarea *igual* tres o más veces al mes? Igual, no parecida. Si cada vez
   cambia, lo que necesita es un buen prompt: el modelo elige mejor camino que tú cuando el caso
   cambia.
2. **¿Requisito?** ¿Lleva dentro un dato que el modelo **no puede adivinar**? Su tono, el formato
   exacto de un entregable, una regla de su negocio, la norma de su país, los nombres de sus
   clientes. Si no hay ninguno, no hay skill: hay una explicación bonita de algo que Claude ya sabe.
3. **¿Repartible?** ¿Otra persona la correría igual? Si solo la entiende quien la pidió, casi
   siempre es un prompt disfrazado.

Y una prueba más, la que más skills mata: **tapa los pasos y deja solo el objetivo, los límites y el
dato duro. ¿Se pierde algo?** Si no se pierde nada, lo que tenías era andamio.

**Si no pasa, dilo en una línea y ofrece la alternativa correcta**, que casi siempre es mejor:

| Lo que en realidad necesitaba | Dónde va |
|---|---|
| Una regla que aplica siempre en este workspace | una línea en `CLAUDE.md` |
| Un dato que hace falta en una tarea concreta | un archivo en `referencias/` que se lee cuando toca |
| Algo que va a hacer una sola vez | en el prompt, y se acabó |
| Repetir una tarea cada día o cada semana | `/loop` o `/schedule`, no una skill |

Decir "esto no necesita una skill" es un buen resultado de esta skill. Sale gratis y ahorra meses.

## Las tres vías

Cuando sí pasa el filtro, la pregunta siguiente es de dónde sale el **dato duro**. Recomienda tú y
explica en media línea por qué:

| Vía | Cuándo | Detalle |
|---|---|---|
| **A. Investigar a fondo** | El dato está afuera: normas, formatos oficiales, un oficio que hay que traer bien traído | `references/via-investigacion.md` |
| **B. Ya existe en internet** | Es algo común y alguien lo resolvió bien | `references/via-internet.md` |
| **C. Con lo que ya sabemos** | El dato es suyo: su tono, su formato, sus ejemplos | ver abajo |

La C es la más frecuente y la que más se subestima. Si lo difícil es *su manera de hacerlo*,
ninguna investigación te la va a dar: pídele **dos o tres ejemplos reales de trabajo suyo bien
hecho, y uno malo**, y sácalo de ahí. Cinco minutos suyos valen más que veinte páginas de Gemini.

Las tres terminan en el mismo sitio: un `SKILL.md` en el formato de abajo. La vía solo cambia de
dónde viene el material.

## Antes de escribir, tres preguntas al usuario (no más)

1. **¿Qué entra y qué sale?** ("le doy las fotos de la obra → sale el informe de avance")
2. **¿Cómo se ve uno bien hecho?** Que te muestre un ejemplo real, o que te lo describa.
3. **¿Cómo se ve uno mal hecho?** Esta es la que más rinde: los errores que le cuestan dinero o
   tiempo son guardarraíles disfrazados.

## La forma de la skill

Plantilla: `plantillas/SKILL-plantilla.md`. Anatomía y errores comunes: `references/anatomia.md`.

Tres piezas, siempre las mismas: **tarea** (el objetivo, en una línea), **guardarraíles** (los
límites, no el camino) y **criterio de término** (cómo sabe que terminó, de forma observable).

Y la descripción del frontmatter es el 90% del trabajo: es lo único que se lee en **cada** sesión y
es lo que decide si la skill se dispara donde debe. Fórmula: qué hace + cuándo usarla + las palabras
que esta persona usaría de verdad al pedirlo. Escríbela con sus palabras, no con las tuyas.

Andamiaje:

```bash
python3 .claude/skills/crear-skill/scripts/nueva-skill.py crear <nombre-en-kebab>
python3 .claude/skills/crear-skill/scripts/nueva-skill.py verificar <nombre>
```

## Guardarraíles

- **El proceso ajeno se tira, el dato duro se queda.** Vale para lo que baje de internet y para lo
  que traiga Gemini: quédate con formatos, reglas, umbrales y vocabulario; tira los "paso 1, paso 2".
- **Nada de investigación pegada entera dentro del `SKILL.md`.** El detalle va a `references/` y el
  `SKILL.md` queda como índice. Si el cuerpo pasa de tres mil palabras, ya te pasaste.
- **Nunca instales una skill de internet tal cual**, ni corras un script suyo sin leerlo antes.
- **Todo dato con origen.** Si vino de una investigación, la skill dice de dónde y de qué fecha. Si
  no se pudo confirmar, se marca sin confirmar en vez de rellenar.
- **Una skill por vez.** Terminada y probada antes de empezar la siguiente.
- **No toques skills de plugins en su sitio** (se pierden al actualizar): cópialas a
  `.claude/skills/` y adapta ahí.
- **Ni pasos ni recordatorios de sentido común.** Nada de "sé cuidadoso", "lee bien", "no inventes".
  Eso ya lo trae y solo ocupa espacio.

## Criterio de término

Listo cuando:

1. `python3 .claude/skills/crear-skill/scripts/nueva-skill.py verificar <nombre>` sale en **PASA**.
2. **Se probó de verdad**: le pediste el trabajo con las palabras que usaría esa persona, la skill
   se disparó sola y el resultado se comparó contra el ejemplo bien hecho que ella mostró.
3. La skill quedó anotada en el estado y en `BITACORA.md`, con **de dónde salió el dato duro**
   (investigación y fecha, URL de origen, o "contexto del usuario").

Si la prueba del punto 2 sale mal, se arregla la skill; no se entrega con una explicación de por
qué falló.

## Referencias

- `references/via-investigacion.md` — el flujo con Gemini Deep Research o Perplexity, de punta a punta.
- `references/via-internet.md` — dónde buscar skills que ya existen y cómo adaptarlas sin heredar
  el proceso de otro.
- `references/anatomia.md` — cómo se escribe una skill que no estorba.
- `plantillas/SKILL-plantilla.md` — el esqueleto.
- `plantillas/prompt-deep-research.md` — el prompt que se le entrega al usuario para investigar.
