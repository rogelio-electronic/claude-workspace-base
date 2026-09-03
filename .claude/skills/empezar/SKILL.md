---
name: empezar
description: Configura este workspace desde cero entrevistando a quien lo abre, y lo deja listo para su trabajo real: escribe el CLAUDE.md, crea las carpetas y propone las primeras skills. Úsala la primera vez que alguien abre esta carpeta, cuando el workspace no tiene perfil todavía, o cuando pidan reconfigurarlo porque cambió su trabajo. Gatillos: empezar, comenzar, arrancar, configurar, primera vez, no sé qué hacer, para qué sirve esto.
---

# Empezar

Deja este workspace configurado para el trabajo real de quien lo abrió, en una sola sesión, sin que
esa persona tenga que aprender nada de Claude Code.

Quien está del otro lado puede no haber usado Claude nunca. Trátalo así hasta que te diga lo
contrario: sin jerga, sin pedirle que edite archivos, sin explicarle qué es un frontmatter.

## Antes de nada: ¿ya está configurado?

```bash
python3 .claude/skills/empezar/scripts/estado.py ver
```

Si dice **sin configurar**, adelante. Si ya tiene perfil, no lo pises: muestra en dos líneas cómo
quedó y pregunta si quiere *ajustar* (cambiar respuestas puntuales), *ampliar* (solo agregar skills
nuevas) o *rehacer* desde cero. Rehacer siempre respalda el `CLAUDE.md` anterior antes de tocarlo.

## El orden importa, y es el único orden obligatorio de esta skill

**Preguntar → construir → skills.** No por ceremonia: el `CLAUDE.md` que escribas se va a leer en
cada sesión futura de esta persona, para siempre. Si lo escribes antes de saber a qué se dedica, le
clavas tus suposiciones a todas sus sesiones. Y una skill propuesta antes de la entrevista sale
genérica, que es la forma cara del ruido.

### Fase 1 — La entrevista

El guion completo, con las preguntas exactas y sus opciones: `references/entrevista.md`.

Resumen: una pregunta abierta en el chat, después **dos rondas** con `AskUserQuestion` (opciones
para hacer clic, nunca más de tres rondas en total). Si una respuesta ya te contestó otra pregunta,
sáltala: preguntar lo que ya sabes gasta la paciencia que vas a necesitar en la fase 3.

Mientras escuchas, ve nombrando en tu cabeza el **perfil** de esta persona. El catálogo de perfiles
—con las carpetas que suele necesitar cada uno y las skills que de verdad le sirven—
está en `references/perfiles.md`. Úsalo como mapa, no como molde: si lo que te contó no encaja en
ninguno, gana lo que te contó.

### Fase 2 — Construir el workspace

Qué se escribe exactamente y con qué presupuesto de líneas: `references/construccion.md`.

Se produce, en este orden: `CLAUDE.md` (reescrito completo, no parcheado), las carpetas de trabajo,
`.claude/estado.json` y la primera entrada de `BITACORA.md`.

El `CLAUDE.md` es lo único de este workspace que se lee **siempre**. Ese es su costo y esa es su
vara: si una línea no cambia lo que Claude haría de todos modos, esa línea no va. Cuarenta líneas
es mucho; veinte bien escritas es un buen workspace.

### Fase 3 — Proponer las primeras skills

Del perfil salen dos a cuatro candidatas. Preséntalas en el idioma de la persona, con nombre en
cristiano y una frase de para qué sirve, y deja que elija. Para cada una que elija, pregunta por
qué vía se arma: **investigar a fondo**, **buscar una que ya exista** o **con lo que ya sabemos**.
Marca tú la recomendada y di en media línea por qué.

No construyas las skills aquí. Anótalas en el estado y pasa el trabajo a la skill `crear-skill`,
que es la que sabe hacerlo bien y la que sabe decir que no cuando algo no merece ser una skill.

Si la persona no quiere ninguna todavía, perfecto: el workspace ya funciona sin skills propias.
Díselo así, sin insistir.

### Fase 4 — Entregar

Cierra siempre con lo mismo: **tres frases exactas** que esa persona puede copiar mañana, escritas
con sus palabras y con sus archivos, no con ejemplos genéricos. Y **prueba una en vivo**, ahí
mismo, para que vea el resultado antes de irse.

## Guardarraíles

- **Nada técnico en las preguntas.** Ni modelos, ni MCP, ni hooks, ni rutas. Si necesitas un dato
  técnico, dedúcelo o míralo tú en la carpeta.
- **No inventes el oficio de nadie.** Todo lo que escribas en el `CLAUDE.md` tiene que venir de una
  respuesta suya o de algo que viste en la carpeta. Si no lo sabes, no lo pongas.
- **No borres nada que ya estuviera en la carpeta.** Si alguien copió esta plantilla sobre archivos
  suyos, esos archivos mandan: léelos antes de proponer estructura, y respeta la que ya exista.
- **No crees carpetas "por si acaso".** Solo las que la persona nombró o las que su perfil usa de
  verdad. Una carpeta vacía es una promesa que nadie cumple.
- **El idioma lo elige quien contesta**, y manda en todo: chat, `CLAUDE.md`, nombres de carpetas,
  skills.
- **Cero placeholders en el resultado.** Ni `<tu nombre>`, ni `TODO`, ni `[completar]`. Si un dato
  falta, se pregunta o se omite la línea.
- **Esta skill se somete a su propia regla.** Si la persona llega sabiendo exactamente lo que
  quiere, salta la entrevista, constrúyelo y ya. El guion es para quien no sabe, no para ti.

## Criterio de término

Listo cuando las cuatro cosas se cumplen:

1. `python3 .claude/skills/empezar/scripts/estado.py verificar` termina en **PASA**.
2. El `CLAUDE.md` está reescrito, cabe en una pantalla, y cada línea contiene algo que Claude no
   habría sabido solo.
3. La persona vio sus tres frases para copiar y **una se ejecutó en vivo con un resultado real**.
4. `BITACORA.md` tiene la entrada de hoy con la fecha de la próxima revisión (tres meses, o el
   próximo modelo nuevo, lo que llegue antes).

Si algo quedó pendiente —una skill que espera una investigación, un dato que la persona iba a
buscar— queda escrito en el estado y dicho en voz alta al cerrar, no guardado en silencio.

## Referencias

Lee solo la que toque:

- `references/entrevista.md` — el guion: preguntas exactas, opciones y qué inferir de cada respuesta.
- `references/perfiles.md` — catálogo de oficios: carpetas, skills que sirven y skills que no.
- `references/construccion.md` — qué archivo se escribe, con qué contenido y con qué límite.
- `plantillas/CLAUDE-md.md` — la forma del CLAUDE.md final.
- `plantillas/BITACORA.md` — la forma de la bitácora.
- `scripts/estado.py` — lee, escribe y verifica `.claude/estado.json`.
