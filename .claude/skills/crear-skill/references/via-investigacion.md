# Vía A — Investigar a fondo

Para cuando el dato duro está **afuera**: normas, formatos oficiales, reglas de un oficio, prácticas
de un sector, cifras que cambian por país. Claude sabe mucho, pero no sabe la resolución que salió
en marzo ni el formato exacto que exige el cliente de esa persona. Eso se trae.

El ciclo es: **preguntar → escribir el prompt → que la persona lo corra afuera → destilar → escribir
la skill**. La persona solo hace una cosa: copiar, pegar y volver.

---

## 1. Antes de escribir el prompt

Tienes que poder contestar tres cosas. Si te faltan, pregúntalas — pero solo estas tres:

- **Qué entra y qué sale.** "Le doy las fotos y las notas de la obra → sale el informe de avance."
- **Dónde y para quién.** País, sector, cliente. Esto decide qué normas aplican y no es opcional.
- **Qué es un mal resultado.** Los errores que le cuestan dinero son guardarraíles disfrazados.

Y mira lo que ya tienes en la mano: `.claude/estado.json` y el `CLAUDE.md` ya te dicen su oficio, su
idioma y sus límites. No vuelvas a preguntar eso.

---

## 2. Escribe el prompt de investigación

Base: `plantillas/prompt-deep-research.md`. **No la entregues genérica** — la mitad de su valor está
en el contexto que le metes: el país, el sector, el cliente, el tipo de archivo con el que trabaja,
la frase con la que esa persona describió su problema.

Guárdalo y entrégalo así:

```bash
mkdir -p investigacion/<nombre-skill>
```

El prompt va a `investigacion/<nombre-skill>/prompt.md` **y** completo en el chat, dentro de un
bloque de código para que se copie de un clic. Que no tenga que abrir un archivo para copiarlo.

---

## 3. Las instrucciones para la persona

Pégaselas casi tal cual, en su idioma. Sin tecnicismos, sin dar por hecho que conoce esas
herramientas. Nombra el botón por lo que dice, no por dónde está: las interfaces se mueven.

> **Lo que sigue lo haces tú, y son tres minutos de trabajo tuyo más una espera.**
>
> **Con Gemini** (es el que mejor funciona para esto):
> 1. Entra a **gemini.google.com** con tu cuenta de Google.
> 2. Busca la opción que dice **Deep Research** o **Investigación profunda** — suele estar en el
>    selector de modelo, arriba, o en el botón de herramientas junto al cuadro de escribir.
>    Actívala *antes* de escribir.
> 3. Pega el texto que te di y envíalo.
> 4. Te va a mostrar un **plan de investigación** y te va a pedir que lo apruebes. Léelo por
>    encima: si ves que se fue por un lado que no es el tuyo, corrígelo con una frase. Si no,
>    aprueba.
> 5. Tarda entre cinco y quince minutos. Puedes cerrar y volver.
> 6. Cuando termine, copia todo el informe (o usa **Exportar**) y pégalo en un archivo de texto
>    llamado `investigacion.md` dentro de la carpeta `investigacion/<nombre-skill>/` de este
>    workspace.
>
> **Con Perplexity**, si prefieres: entra a **perplexity.ai**, activa el modo **Research**, pega el
> mismo texto, y al terminar exporta como Markdown o copia el resultado en el mismo archivo.
>
> **Cuando esté guardado, vuelve aquí y escribe: `listo`.**

Si no sabe crear el archivo, ofrécele la salida fácil: **que pegue el informe entero en el chat**.
Tú lo guardas. Nunca la mandes a pelear con un editor de texto.

Y deja anotado el pendiente antes de que se vaya, que estas cosas se pierden:

```bash
python3 .claude/skills/empezar/scripts/estado.py skill "<nombre>" --via investigacion --estado investigando
```

---

## 4. Cuando vuelva con el informe: destilar

Aquí es donde se gana o se pierde. Un informe de investigación trae veinte o cuarenta páginas.
**De ahí salen una o dos páginas de skill.** Si tu `SKILL.md` se parece al informe, no destilaste:
copiaste.

Léelo entero y sepáralo en tres montones:

| Montón | Qué es | A dónde va |
|---|---|---|
| **Dato duro** | Umbrales, tasas, plazos, normas con su versión, formatos exactos, vocabulario del gremio, criterios de decisión | El cuerpo de la skill, o un `references/` si es largo |
| **Guardarraíl** | Los errores caros y cómo se detectan; lo que nunca se hace | La sección de guardarraíles |
| **Relleno** | Historia del tema, definiciones de diccionario, "consejos", pasos genéricos, todo lo que el modelo ya sabe | **Se tira.** Sin culpa |

El relleno es la mayor parte. Es normal: la investigación está escrita para un humano que no sabe
nada, y tú se la estás dando a un modelo que ya sabe casi todo salvo lo específico.

Reglas al destilar:

- **Toda cifra o norma se queda con su fuente y su fecha**, dentro de la skill. Un umbral sin fecha
  es un umbral que va a estar mal dentro de un año y nadie va a saber.
- **Lo que el informe marcó como sin confirmar, se queda marcado así.** No lo redondees a verdad.
- **Si una sección del informe contradice a otra**, dilo en la skill en una línea en vez de elegir
  tú en silencio.
- **El informe crudo se conserva** en `investigacion/<nombre>/investigacion.md`. No lo borres: es de
  dónde salió todo, y dentro de un año va a hacer falta.

---

## 5. Escribir la skill y probarla

Con el dato duro ya separado, sigue el `SKILL.md` de `crear-skill`: tarea, guardarraíles, criterio
de término, y la descripción escrita con las palabras de esa persona.

Y ciérralo bien:

```bash
python3 .claude/skills/crear-skill/scripts/nueva-skill.py verificar <nombre>
python3 .claude/skills/empezar/scripts/estado.py skill "<nombre>" --estado lista
```

La prueba real es pedirle el trabajo con sus palabras y comparar el resultado contra el ejemplo bien
hecho que ella mostró al principio. Si no hay con qué compararlo, todavía no está probada.

---

## Cuándo **no** usar esta vía

- El dato es suyo, no del mundo (su tono, su plantilla, su lista de precios) → vía C, y pídele
  ejemplos reales.
- Es algo común y bien documentado que el modelo ya maneja → no hace falta investigar nada, y
  probablemente no hace falta ni la skill.
- La persona necesita el resultado hoy → vía C ahora, y la investigación después si vale la pena.

Media hora de investigación bien gastada vale meses. Media hora gastada en investigar lo que el
modelo ya sabía es media hora, y encima deja una skill que envejece.
