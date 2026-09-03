# Workspace Base para Claude Code

Una carpeta vacía que se convierte, en unos minutos y contestando preguntas de opción múltiple,
en un espacio de trabajo hecho a la medida de **tu** trabajo.

No hay que saber programar. No hay que entender qué es una skill. Se abre la carpeta con Claude,
se escribe una palabra, y se contesta.

---

## Los tres pasos

### 1. Instala Claude Code (una sola vez en la vida)

**Si nunca has usado la Terminal**, descarga la app de escritorio en **https://claude.com/download**
e instálala como cualquier programa. Es la misma herramienta, con una ventana normal.

**Si te manejas en la Terminal**, en Mac o Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

En Windows, desde PowerShell: `irm https://claude.ai/install.ps1 | iex`

Necesitas una cuenta Pro, Max, Team o de API. El plan gratuito de Claude.ai no incluye Claude Code.
El paso a paso completo, con los errores típicos, está en
[docs/instalar-claude-code.md](docs/instalar-claude-code.md).

### 2. Copia esta carpeta y ábrela

Descarga el ZIP o clónala, y renombra la carpeta como quieras:

```bash
git clone https://github.com/TU-USUARIO/claude-workspace-base.git mi-trabajo
```

**En la app de escritorio:** File → Open Folder, y eliges esa carpeta.

**En la Terminal:**

```bash
cd mi-trabajo
claude
```

Claude solo ve la carpeta desde la que lo abres. Abrirlo en el sitio correcto es lo que hace que
todo lo demás funcione.

### 3. Escribe una palabra

```
empezar
```

Eso es todo.

---

## Qué va a pasar cuando escribas `empezar`

1. **Te pregunta.** Dos o tres pantallas de opciones para hacer clic. Nada técnico: a qué te
   dedicas, qué haces más seguido, qué no debe tocar, cómo prefieres que te hable.
2. **Arma la carpeta.** Escribe las instrucciones permanentes del workspace, crea las carpetas de
   trabajo que tu caso necesita y deja anotado lo que decidiste.
3. **Te propone habilidades.** Mira lo que le contaste y te sugiere dos o tres *skills* — cosas que
   Claude va a saber hacer siempre igual, a tu manera. Tú eliges cuáles y por qué vía se arman:

   | Vía | Cuándo conviene | Qué te toca hacer |
   |---|---|---|
   | **Investigar a fondo** | El tema tiene reglas, normas o formatos que hay que traer de afuera | Copiar un texto que Claude te da, pegarlo en Gemini (Deep Research) o Perplexity, y guardar el resultado |
   | **Buscar una que ya exista** | Es algo común, alguien ya lo resolvió | Nada. Claude busca, elige y la adapta a lo tuyo |
   | **Con lo que ya sabemos** | Lo difícil es tu formato, tu tono, tu manera | Mostrarle dos o tres ejemplos de tu trabajo real |

4. **Te enseña a usarlo.** Termina dándote tres frases exactas, escritas con tus palabras, que
   puedes copiar y pegar mañana. Y prueba una en vivo para que veas que funciona.

---

## Qué trae por dentro

```
CLAUDE.md          Las instrucciones permanentes. Se reescriben solas en el paso 2.
.claude/skills/    Cuatro habilidades base:
   empezar         La entrevista y el armado inicial.
   crear-skill     La fábrica: convierte una necesidad tuya en una habilidad nueva.
   mantenimiento   La limpieza: revisa qué sobra y lo apaga sin borrarlo.
   ayuda           El mapa: "¿qué le puedo pedir a esto?", en cristiano.
docs/              Para el curioso. No hace falta leerlo para usarlo.
investigacion/     Aquí caen los informes de Gemini o Perplexity cuando uses esa vía.
```

Cuatro y no cuarenta, a propósito. La configuración de Claude tiene un impuesto: **todo lo que
dejas puesto se lee en cada sesión, para siempre**. Este workspace nace deliberadamente flaco y
engorda solo con lo que tú demuestres que hace falta. El método está explicado en
[docs/como-funciona.md](docs/como-funciona.md).

---

## Después del primer día

| Escribe esto | Y pasa esto |
|---|---|
| `ayuda` | Te recuerda qué puede hacer este workspace y con qué palabras pedírselo |
| `quiero que aprendas a...` | Arranca la fábrica de skills |
| `revisa este workspace` | Audita qué configuración sobra y la apaga sin borrar nada |
| `empezar` (otra vez) | Reconfigura, si tu trabajo cambió |

---

## Preguntas rápidas

**¿Esto sube mis archivos a algún lado?** No. Claude Code corre en tu computador y lee la carpeta
donde lo abriste. Lo único que sale de tu máquina es lo que le escribes en el chat.

**¿Puedo usarlo para varias cosas distintas?** Puedes, pero no conviene. Una copia por frente de
trabajo: las instrucciones del workspace son lo que lo hace bueno, y mezclarlas lo vuelve genérico.
Copiar la carpeta otra vez cuesta diez segundos.

**¿Y si me equivoco contestando?** Nada es permanente. `empezar` se puede correr de nuevo y
`mantenimiento` apaga cosas sin borrarlas, siempre imprimiendo cómo deshacerlo.

**¿Necesito pagar algo?** Claude Code requiere una cuenta de Claude (Pro, Max o API). El workspace
en sí es gratis y es tuyo.

---

## Licencia

MIT. Úsalo, cópialo, cámbialo, repártelo.

El método de adelgazamiento (*ablación*, filtro de las tres R, formato tarea + guardarraíles +
criterio de término) viene de la skill `ablacion` de Rogelio Gómez, y está incorporado aquí en
`.claude/skills/mantenimiento/`.
