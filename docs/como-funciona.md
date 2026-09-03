# Cómo funciona esto por dentro

No hace falta leer esto para usar el workspace. Sirve para cuando quieras cambiarlo tú, o para
entender por qué está armado así y no de otra manera.

---

## Las tres piezas

Claude Code se personaliza con tres cosas, y conviene no confundirlas porque cuestan distinto.

### 1. `CLAUDE.md` — las instrucciones permanentes

Un archivo de texto en la raíz de la carpeta. Claude lo lee **entero, en cada sesión, antes de que
escribas nada**. Va lo que siempre aplica: tu oficio, tu tono, tus límites, las reglas que no puede
adivinar.

Es la pieza más poderosa y la más cara. Cada línea se paga en todas las sesiones futuras. Por eso
la vara es: *¿Claude haría algo distinto si esta línea no estuviera?*

También se cargan los `CLAUDE.md` de las carpetas de arriba y el de `~/.claude/`. Por eso conviene
tener el workspace en su propia carpeta y no colgando de una llena de cosas ajenas.

### 2. Las skills — habilidades que se activan solas

Cada skill es una carpeta con un archivo `SKILL.md` dentro de `.claude/skills/`. Tiene dos partes:

- Una **descripción** de una o dos líneas. Esto se carga siempre, en cada sesión, de todas las
  skills instaladas. Es lo que Claude usa para decidir si esa skill aplica a lo que acabas de pedir.
- Un **cuerpo** con las instrucciones completas. Esto solo entra cuando la skill se dispara.

A eso se le llama *revelación progresiva*, y es la razón de que puedas tener varias skills sin que
te cuesten un ojo de la cara. Pero significa que **la descripción es el 90% del trabajo**: una
descripción vaga hace que la skill aparezca donde no toca, y eso es peor que no tenerla.

### 3. Todo lo demás — hooks, MCP, plugins

Automatizaciones, conexiones a otras herramientas, paquetes de skills de terceros. Potentes, y con
un costo que casi nadie mide: tokens en cada sesión, latencia, y una cosa más que se puede romper.

Este workspace no trae ninguno a propósito. Cuando lo necesites, lo agregas.

---

## Por qué solo cuatro skills

Porque el problema de hoy **no es que a Claude le falte instrucción, es que le sobre**.

Los modelos actuales ya saben hacer casi todo lo que la gente escribe en sus skills: leer con
cuidado, elegir la herramienta, no inventar datos, ordenar su trabajo. Una instrucción escrita para
un modelo de hace un año no se borra sola cuando el modelo mejora: se queda ahí, apretando el
caballo. Se le llama *hobbling*: frenar al modelo con instrucciones que ya no hacen falta.

El daño casi nunca es el tamaño del archivo. Es que **una skill vieja se dispara donde no debía y te
clava su camino** cuando había uno mejor.

Así que este workspace nace deliberadamente flaco y engorda solo con lo que demuestres que hace
falta. Los cuatro que trae son de operación —arrancar, crear, mantener, orientar—, no de contenido.
Las de contenido las creas tú, con tus datos, con `crear-skill`.

---

## El filtro: cuándo algo merece ser una skill

Tres preguntas. Las tres tienen que dar que sí:

1. **¿Repetible?** ¿Haces esa tarea *igual* tres o más veces al mes? Igual, no parecida.
2. **¿Requisito?** ¿Lleva dentro un dato que Claude no puede adivinar? Tu formato, tu tono, tu
   regla, tu norma. Si no hay ninguno, no hay skill.
3. **¿Repartible?** ¿Otra persona la correría igual que tú?

Y una prueba más, la que más skills mata: **tapa los pasos y deja solo el objetivo, los límites y el
dato duro. ¿Se pierde algo?** Si no se pierde nada, lo que tenías era andamio, no habilidad.

Lo que no pasa el filtro tiene mejores destinos: una línea en `CLAUDE.md` si aplica siempre; un
archivo de referencia si aplica a una tarea; el prompt de hoy si es de una vez; una tarea
programada si lo que repites es *cuándo* y no *cómo*.

---

## Cómo se escribe una buena instrucción

Tres piezas, y la tercera es la que casi nadie escribe:

**Tarea.** El objetivo pelado, en una línea. Y que se vea un poco más grande de lo cómodo: ahí es
donde sorprende.

**Guardarraíles.** Los límites, no el camino. "No toques la base de datos" es un guardarraíl.
"Abre el archivo y edita la línea 12" es un paso, y los pasos frenan.

**Criterio de término.** Cómo sabe que terminó. Sin esto, hace un intento razonable, entrega algo
que *parece* listo, y se va.

Y dale un espejo: algo con lo que pueda verse a sí mismo sin preguntarte. Tests que corren solos,
totales que tienen que cuadrar, un pantallazo contra la referencia, una corrida real. "No pares
hasta que esté listo" no significa nada si no tiene con qué medir "listo".

| Antes (receta) | Después (tres piezas) |
|---|---|
| "Abre la carpeta de facturas, busca el último número, súmale uno, copia la plantilla, cambia el nombre, calcula el IVA al 16%, guarda como PDF." | "Emite la factura de X por Y. Guardarraíles: numeración correlativa sin saltos, IVA 16%, mismo formato que las tres últimas, no toques las ya emitidas. Listo cuando el PDF abra bien y sus totales cuadren con la orden." |

---

## Probar sin romper nada

La forma honesta de saber si algo hace falta es apagarlo y trabajar sin ello:

```bash
claude --safe-mode      # una sesión con TODA la personalización apagada. No borra nada
```

Y para apagar cosas de forma persistente pero reversible, `mantenimiento` tiene las palancas. Nada
en este workspace se borra: se aparta, y siempre te imprime cómo devolverlo.

---

## La revisión periódica

Cada tres meses, o cuando salga un modelo nuevo —lo que llegue antes—, media hora:

1. Trabaja un par de sesiones con `claude --safe-mode`.
2. Anota **solo** lo que falló de verdad, con fecha.
3. Devuelve una instrucción por vez, y solo si falló dos veces.
4. Compara el antes y el después con `inventario.py`.

Lo que no volvió en un ciclo completo, ya sabes lo que era.

> El método —ablación, filtro de las tres R, tarea + guardarraíles + criterio de término— viene de
> la skill `ablacion` de Rogelio Gómez.
