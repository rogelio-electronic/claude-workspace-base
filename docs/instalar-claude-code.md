# Instalar Claude Code, desde cero

Verificado contra la documentación oficial el 2 de septiembre de 2026. Si algo no coincide, la
página oficial manda: **https://code.claude.com/docs/en/setup**

---

## Antes que nada: la cuenta

Claude Code necesita una cuenta **Pro, Max, Team, Enterprise o de Console (API)**. El plan gratuito
de Claude.ai **no** lo incluye. Si no tienes ninguno, ese es el primer paso y el único que cuesta
dinero.

---

## Dos caminos. Elige el tuyo

### Camino A — La app de escritorio (sin terminal)

**Si nunca has usado la Terminal, este es tu camino.** Es la misma herramienta con una ventana
normal: se instala como cualquier programa y se elige la carpeta desde un menú.

1. Descárgala desde **https://claude.com/download**
2. Instálala como cualquier aplicación.
3. Ábrela e inicia sesión con tu cuenta de Claude.
4. Elige la carpeta de este workspace cuando te la pida.
5. Escribe `empezar` en el cuadro de chat.

Y ya. El resto de este documento no te hace falta.

### Camino B — La Terminal

Más directo si ya te manejas, y es el que verás en casi todos los tutoriales.

**Mac, Linux o WSL** — abre la Terminal y pega:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows, en PowerShell** (el que muestra `PS C:\`):

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows, en CMD** (el que muestra `C:\` sin el `PS`):

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Con Homebrew, en Mac**, si ya lo usas:

```bash
brew install --cask claude-code
```

Comprueba que quedó bien:

```bash
claude --version
```

Tiene que responder un número de versión, algo como `2.1.226 (Claude Code)`. Si dice
`command not found`, cierra la Terminal, ábrela de nuevo y prueba otra vez. Si sigue igual,
`claude doctor` te dice qué pasa, y hay una guía completa de errores en
https://code.claude.com/docs/en/troubleshoot-install

---

## Abrir este workspace

La regla de oro: **Claude solo ve la carpeta desde la que lo abriste.** Ni más arriba, ni al lado.
Así que abrirlo en el sitio correcto no es un detalle, es lo que hace que funcione.

**En la app de escritorio:** File → Open Folder (o el selector de carpeta al iniciar), y eliges la
carpeta de tu workspace.

**En la Terminal:**

```bash
cd ruta/a/tu-carpeta
claude
```

En Mac hay un atajo cómodo: escribe `cd ` (con el espacio), arrastra la carpeta desde el Finder a la
ventana de la Terminal, y suelta. La ruta se escribe sola. Después, Enter, y luego `claude`.

**En VS Code:** File → Open Folder sobre la carpeta, y *después* abre la extensión de Claude. Si lo
haces al revés, Claude se abre donde estabas antes.

---

## La primera vez

Te va a pedir iniciar sesión: se abre el navegador, apruebas, y vuelves a la Terminal. Eso pasa una
sola vez.

Después escribe:

```
empezar
```

Y contesta lo que te pregunte. Son opciones para elegir, no hay respuestas incorrectas, y se puede
volver a correr cuando quieras.

---

## Tres cosas que conviene saber desde el día uno

- **Se escribe en cristiano.** No hay comandos que memorizar. "Revisa este contrato y dime qué me
  falta" es una instrucción perfectamente válida.
- **Para salir**, escribe `/exit` o pulsa Ctrl+C dos veces. Para volver, `claude` otra vez desde la
  misma carpeta.
- **Pregunta antes de cambiar cosas** que puedan romper algo. Si te pide permiso, léelo: es el
  momento de decir que no.

## Si algo sale mal

| Síntoma | Qué hacer |
|---|---|
| `command not found: claude` | Cierra y reabre la Terminal. Si sigue, `claude doctor` |
| No encuentra tus archivos | Lo abriste en la carpeta equivocada. Sal, `cd` a la correcta, y entra otra vez |
| No entiende para qué es la carpeta | Escribe `empezar` |
| Se quedó pensando mucho rato | Normal en tareas largas. Ctrl+C corta lo que esté haciendo |
| Hizo algo que no querías | Díselo con esas palabras. Y si tocó archivos, `git` o la papelera son tus amigos |

Guía oficial paso a paso para quien nunca usó una terminal:
https://code.claude.com/docs/en/terminal-guide
