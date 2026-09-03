# Esqueleto de una skill

```markdown
---
name: nombre-en-kebab-case
description: <Qué hace, en una frase>. Úsala cuando <situación concreta>. Gatillos: <las
  palabras que esta persona usaría de verdad al pedirlo>.
---

# <Nombre>

<Una línea: para qué existe y qué resultado deja.>

## Qué hace

<El objetivo, no el procedimiento. Dos o tres frases.>

## El dato que el modelo no puede adivinar

<La razón de ser de la skill: el formato exacto, el tono con ejemplos reales, la ruta, la
regla del negocio, la norma con su versión y su fecha. Si esta sección queda vacía, no
hagas la skill: haz un prompt.>

## Guardarraíles

- <Lo que no se toca.>
- <Lo que no se inventa, y de dónde tiene que salir cada dato.>
- <Contra qué se compara el resultado.>

## Criterio de término

Listo cuando <condición observable que se puede comprobar sin preguntarle a nadie>.

## Referencias

- `references/<detalle>.md` — <cuándo leerlo>.
- `scripts/<script>.py` — <qué automatiza>.
```

---

## Ejemplo terminado

```markdown
---
name: valuaciones
description: Arma la valuación mensual de obra con las partidas del contrato y el formato que
  exige PDVSA. Úsala cuando pidan valuación, corte de obra o avance del mes. Gatillos:
  valuación, corte, avance de obra, lo del mes.
---

# Valuaciones

Convierte las mediciones del mes en la valuación que se le entrega al cliente, lista para firmar.

## Qué hace

Toma las mediciones de campo y el contrato, y produce el documento de valuación con las partidas,
las cantidades acumuladas y el monto del período. Es el entregable que se factura: si sale mal,
se devuelve.

## El dato que el modelo no puede adivinar

- Las partidas y unidades salen **del contrato**, nunca de las notas de campo. Si una medición no
  tiene partida, se reporta aparte, no se inventa una.
- Formato PDVSA: número de contrato en cada página, montos en dólares con dos decimales, acumulado
  del período anterior en la columna previa.
- La retención es del 10% sobre el monto del período. (Contrato GC-2024-118, cláusula 9.)
- Nada se redondea hacia arriba. Nunca.

## Guardarraíles

- Ninguna cantidad sin su medición de origen; si falta el respaldo, se marca y se pregunta.
- No se modifican valuaciones ya entregadas. Se emite una nueva.
- El acumulado tiene que cuadrar con la valuación anterior al centavo antes de entregar.

## Criterio de término

Listo cuando el acumulado cuadra con la valuación del mes anterior, cada partida tiene su medición
de respaldo, y el documento abre bien con el formato del cliente.
```

Fíjate en lo que **no** tiene: ni un paso, ni un "sé cuidadoso", ni una explicación de qué es una
valuación. Solo lo que Claude no podía saber, y contra qué se mide el resultado.
