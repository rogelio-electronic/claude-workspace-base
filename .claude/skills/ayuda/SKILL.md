---
name: ayuda
description: Explica en lenguaje llano qué puede hacer este workspace y con qué frases exactas pedírselo, leyendo su configuración real en vez de dar ejemplos genéricos. Úsala cuando pregunten qué puedes hacer, qué le pueden pedir, cómo funciona esto, o cuando alguien se quede en blanco sin saber por dónde empezar. Gatillos: ayuda, qué puedes hacer, qué te puedo pedir, cómo funciona esto, no sé por dónde empezar, estoy perdido.
---

# Ayuda

Devuelve el mapa de **este** workspace: qué sabe hacer, con qué palabras se le pide y qué conviene
hacer ahora. En cristiano, para alguien que puede no haber usado Claude nunca.

## De dónde sacar la respuesta

```bash
python3 .claude/skills/empezar/scripts/estado.py ver
```

Eso, más las skills que existen en `.claude/skills/` y el `CLAUDE.md`, es la respuesta. **Nunca
contestes con ejemplos genéricos de lo que Claude puede hacer en general** — de eso hay internet
lleno y no le sirve a nadie. Lo que esta persona necesita saber es qué puede pedirle *aquí*, con
*sus* archivos.

Si el estado dice **sin configurar**, la respuesta es corta: dile que escriba `empezar`, que son
unas preguntas de opción múltiple y que después esto queda hecho a su medida. Nada más.

## La forma de la respuesta

Tres bloques, en este orden, y cortos:

1. **Qué es este espacio**, en una frase suya (sale del estado, no la inventes).
2. **Qué le puedes pedir**, en una tabla de dos columnas: *escribe esto* → *y pasa esto*. Entre
   cuatro y seis filas. Las frases van con sus archivos y su vocabulario reales, listas para copiar
   y pegar; nada de `<pon aquí tu archivo>`.
3. **Qué conviene ahora**, una sola sugerencia. La más útil según lo que veas: una skill pendiente
   que quedó a medias, una revisión que ya tocaba, o simplemente la tarea que más repite.

Y cierra ofreciendo lo que siempre está disponible aquí: crear una habilidad nueva
(`quiero que aprendas a...`), revisar y limpiar (`revisa este workspace`) o reconfigurar (`empezar`).

## Guardarraíles

- **Nada de jerga.** Ni "skill", ni "contexto", ni "MCP", ni "frontmatter", salvo que esa persona ya
  las haya usado. Se dice "habilidad", "lo que ya te enseñé", "las instrucciones de esta carpeta".
- **No listes las cuatro skills base como si fueran funciones.** A quien pregunta no le interesa el
  inventario: le interesa qué escribir mañana.
- **Máximo una pantalla.** Si no cabe, es que estás explicando en vez de orientando.
- **No inventes capacidades.** Si algo no está configurado, se dice que no está y se ofrece armarlo.

## Criterio de término

Listo cuando la persona tiene delante entre cuatro y seis frases que puede copiar hoy mismo con sus
propios archivos, y una sola cosa recomendada para hacer ahora.
