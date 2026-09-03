# El filtro: qué se queda y qué palanca le toca

## Las tres R

Una skill se queda solo si responde **sí** a las tres. En este orden.

**1. Repetible.** ¿Se hace esa tarea *exactamente igual* tres o más veces al mes?
Igual, no parecida. Si es parecida, lo que hace falta es un buen prompt: el modelo elige mejor
camino que tú cada vez que el caso cambia un poco.

**2. Requisito.** ¿Lleva dentro un dato que el modelo **no puede adivinar**?
El tono de esta persona, el formato exacto de una factura, la ruta de una carpeta, una regla
contable de su país, el nombre de un cliente. Si al quitarle los pasos y dejar solo ese dato no se
pierde nada, entonces la skill nunca fue el proceso: era el dato.

**3. Repartible.** ¿Otra persona, un equipo o un cliente la va a correr igual?
Ahí deja de ser una muleta y es lo que de verdad es: un procedimiento empaquetado. Una skill que
solo entiende quien la escribió suele ser un prompt disfrazado.

## Prueba de hobbling

Aunque pase las tres R, hazle esto:

- Tapa los pasos y deja solo el objetivo, los límites y el dato duro. ¿Se pierde el resultado?
- ¿Los pasos dicen *qué lograr* o dicen *cómo teclearlo*? Lo segundo envejece con cada modelo.
- ¿Se escribió para un modelo que ya no se usa? Mira la fecha del archivo, no el recuerdo.
- ¿Prohíbe algo que hoy el modelo hace mejor solo (elegir herramienta, orden de lectura, formato
  intermedio)?

Si sobrevive, es real. Si no, extrae el dato duro y tira el andamio.

## Tabla de veredictos

| Veredicto | Cuándo | Palanca |
|---|---|---|
| **Queda** | pasa las 3R y la prueba de hobbling | nada |
| **Reescribir** | el dato vale, los pasos estorban | reescribir con la plantilla de `crear-skill` |
| **Solo-nombre** | útil, pero su descripción es larga y se dispara de más | `palanca.py apagar X --modo solo-nombre` |
| **Solo-usuario** | se quiere a mano, pero que no se meta sola | `palanca.py apagar X --modo solo-usuario` |
| **Apagada** | hay dudas y se quiere un A/B limpio | `palanca.py apagar X --modo off` |
| **Cuarentena** | meses sin usarla y nadie la defiende en una línea | `palanca.py cuarentena X` |
| **Archivo muerto** | `SKILL.md` fuera de `.claude/skills/`: no se carga | no cuesta nada; ordenarlo o borrarlo lo decide el usuario |
| **No es tuya** | de un plugin o bajada de internet, escrita para el proceso de otro | copiarla a `.claude/skills/` y adaptarla, o quitarla |

Regla práctica: **lo bajado de internet muere primero.** No por mal escrito, sino porque estandariza
el proceso de otra persona. Las que sobreviven casi siempre son las que nacieron haciendo la tarea a
mano varias veces.

## Cómo leer las marcas del inventario

- `micromanaging` (muchos pasos numerados): candidata a reescritura, no a borrado automático.
- `vieja` (más de 120 días sin tocar): pregunta cuándo se usó por última vez de verdad.
- `desc-larga` (más de 500 caracteres): se dispara donde no debe y ocupa en cada sesión.
- `SIN-DESC`: nunca se dispara sola. O se le pone descripción o es un comando disfrazado.
- `cuerpo-gordo` (más de 3000 palabras): partir el detalle en `references/`.

## Casi siempre ganan

Tono de voz con ejemplos reales · el formato exacto de un entregable que factura · reglas de un
negocio que el modelo no puede deducir · un procedimiento que corre todo un equipo · convenciones
internas (rutas, nombres de archivo, nomenclatura).

## Casi siempre pierden

"Cómo programar X" · checklists genéricas de calidad · "sé cuidadoso, revisa bien" · recetas de
herramientas que cambian solas · cualquier cosa que empiece con "Paso 1: abre".

## Y lo que se rescata, ¿dónde va?

El dato duro que justificaba la skill casi nunca necesita ser una skill:

- Se usa **siempre en este workspace** → una línea en el `CLAUDE.md`.
- Se usa **en una tarea concreta** → un archivo de referencia que se lee cuando toca.
- Se usa **una vez** → va en el prompt y se acabó.
- Se repite **cada día o cada semana** → `/loop` o `/schedule`, que reparten trabajo en vez de
  estandarizar un proceso.

## Cuando salga un modelo nuevo

Media hora, cada tres meses o con cada modelo, lo que llegue antes:

1. `claude --safe-mode` en este workspace. Trabajar normal un par de sesiones.
2. Anotar **solo** lo que falló de verdad, con fecha: `palanca.py bitacora "..."`.
3. Devolver una instrucción por vez, y solo si falló dos veces.
4. Correr `inventario.py` y comparar el antes/después de tokens siempre activos.
5. Lo que no volvió en un ciclo completo, ya sabes lo que era.

Regla de fondo: **cada instrucción que devuelves la va a leer el modelo en cada sesión, para
siempre.** Que se la gane.
