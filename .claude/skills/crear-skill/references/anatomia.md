# Anatomía de una skill que no estorba

Cómo se escribe una skill para que ayude cuando toca y no aparezca cuando no toca.

## Dónde vive

```
.claude/skills/<nombre>/
├── SKILL.md          ← obligatorio. Frontmatter + cuerpo corto
├── references/       ← el detalle; se lee solo cuando hace falta
├── scripts/          ← lo determinista
└── plantillas/       ← formatos de salida
```

Se cargan solas las que están en `.claude/skills/` de este workspace, las de `~/.claude/skills/`
(todas tus sesiones) y las de los plugins activos. **Una carpeta `skills/` que no cuelgue de
`.claude/` no se carga**: es un archivo muerto en el disco.

## Frontmatter

```yaml
---
name: nombre-en-kebab-case          # obligatorio, idéntico al nombre de la carpeta
description: >-                     # obligatorio: lo ÚNICO que se lee siempre
  Qué hace, cuándo usarla y con qué palabras se pide.
allowed-tools: Bash, Read, Edit     # opcional: limita herramientas. Si dudas, no lo pongas
disable-model-invocation: true      # opcional: solo con /nombre; el modelo no la dispara sola
---
```

## La descripción es el 90% del trabajo

De cada skill instalada, en cada sesión, entra **solo el nombre y la descripción**. El cuerpo entra
cuando se dispara. Así que la descripción hace dos trabajos: ocupa espacio siempre, y decide si la
skill aparece donde debe.

Fórmula: **qué hace + cuándo usarla + las palabras que esa persona usaría al pedirlo**, en tercera
persona.

- Mala: `Ayuda con documentos.` → se dispara en todo o en nada.
- Buena: `Genera la minuta de reunión con el formato del departamento. Úsala cuando pidan minuta,
  acta o resumen de reunión a partir de notas o de una transcripción.`

Corta y específica. Larga y ambiciosa trae disparos falsos, que es la forma más cara de ruido: mete
un cuerpo entero de instrucciones donde no tocaba. Apunta a menos de 500 caracteres.

## Cuerpo

- Menos de tres mil palabras. Si crece, parte el detalle en `references/` y deja el `SKILL.md` como
  índice de qué leer y cuándo.
- Son instrucciones **para Claude**, no un tutorial para el usuario. Escribe en directivo.
- Lleva siempre sus **guardarraíles** y su **criterio de término**. Si no sabes escribir cuándo
  termina, la skill todavía no está pensada.
- Nada de "paso 1, paso 2", salvo cuando el orden es obligatorio de verdad (algo legal, contable o
  de seguridad). En ese caso dilo y explica por qué importa el orden.
- Nada de recordarle al modelo que sea cuidadoso, que lea bien o que no invente. Eso ya lo trae.

## Lo determinista va en un script

Contar, medir, mover archivos, validar un formato, editar un JSON: eso a un script. Un script no
alucina, se prueba, y no gasta contexto explicando cómo hacerlo. La skill decide **qué** y
**cuándo**; el script hace el **cómo** aburrido.

Regla: si escribiste tres párrafos explicando un procedimiento exacto y repetible, eso quería ser
veinte líneas de código.

## Errores comunes

| Error | Reemplazo |
|---|---|
| Receta de pasos para una tarea variable | objetivo + guardarraíles + criterio de término |
| Descripción genérica | qué + cuándo + palabras gatillo |
| Todo en un `SKILL.md` gigante | índice corto + `references/` |
| Instrucciones que repiten lo obvio | borrarlas |
| Copiar una skill de internet tal cual | quedarse con su dato duro y tirar su proceso |
| Escribirla "por si acaso" | esperar a hacer la tarea a mano tres veces |

## Antes de darla por buena

1. Aparece en `/skills` y su descripción se lee bien de un vistazo.
2. En una sesión nueva, pídele el trabajo con las palabras normales de esa persona: **¿se dispara
   sola? ¿o se dispara donde no debía?** Las dos preguntas importan igual.
3. Córrele el filtro de las tres R a tu propia skill recién nacida. Duele y ahorra meses.
4. Ponle fecha de revisión en la bitácora. Toda skill nace con caducidad: el próximo modelo.

---

> Método tomado de la skill `ablacion` de Rogelio Gómez. La versión de mantenimiento vive en
> `.claude/skills/mantenimiento/`.
