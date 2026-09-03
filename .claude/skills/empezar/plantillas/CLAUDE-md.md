# La forma del CLAUDE.md final

Copia la forma, no el contenido. Las secciones que no apliquen se borran enteras — un encabezado
vacío es peor que no tenerlo.

---

## Esqueleto

```markdown
# <Nombre del workspace> — <qué es, en seis palabras>

<Una frase: quién trabaja aquí y para qué. Con oficio y, si lo dijo, sector y país.>

## Cómo responderme

- <Tono e idioma: "Español. Breve y al grano, sin resumir lo que acabas de hacer.">
- <Nivel: "No soy técnico: si vas a correr un comando, dime en una línea qué hace.">

## Lo que no se toca

- <Límite duro, uno por línea. Carpetas privadas, acciones que necesitan permiso.>
- <Lo que nunca sale de esta máquina.>

## Reglas de mi oficio

- <El dato que no puedes adivinar: moneda, norma y su versión, formato del cliente,
  tolerancias, nombres propios que se repiten. Tres o cuatro líneas, no diez.>

## Dónde está cada cosa

- `<carpeta>/` — <qué vive ahí>   ← solo si la estructura no se entiende sola
```

---

## Ejemplo real, completo

```markdown
# Administración GCCA — obra y proveedores

Rogelio lleva la administración de una constructora pequeña que opera dentro de una refinería en
Venezuela. Lo que sale de aquí lo lee el cliente, no el equipo.

## Cómo responderme

- Español. Breve y al grano; nada de resumir al final lo que acabas de hacer.
- Si vas a correr un comando o tocar un archivo, dime en una línea qué hace antes.

## Lo que no se toca

- No borres ni muevas archivos sin preguntarme.
- No envíes nada hacia afuera —correo, subir a la web, publicar— sin permiso explícito.
- `nomina/` es privada: no sale de esta máquina ni entra en ningún resumen.

## Reglas de mi oficio

- Todo en dólares. Si un documento viene en bolívares, convierte y deja dicho a qué tasa y de qué
  fecha.
- Ningún número en un informe sin el documento del que salió.
- Las valuaciones van con las partidas y unidades del contrato, nunca con las mías.
- El cliente es PDVSA: formato formal, sin abreviaturas, con número de contrato en cada página.

## Dónde está cada cosa

- `valuaciones/` — lo que se le factura al cliente, una carpeta por mes.
- `proveedores/` — cotizaciones y órdenes de compra.
- `entregables/` — lo que ya se entregó. No se edita, se versiona.
```

Veintitrés líneas. Cada una cambia lo que Claude haría. Esa es la vara.

---

## La prueba antes de guardarlo

Léelo entero de nuevo y tacha mentalmente cada línea, una por una:

1. ¿Claude haría **exactamente lo mismo** sin esta línea? → fuera.
2. ¿Esto es un límite o es un paso? Los límites se quedan; los pasos se van a una skill.
3. ¿Hay algún dato que la persona no me dijo y yo supuse? → fuera, o pregúntalo ahora.
4. ¿Queda algún `<corchete>`, `TODO` o ejemplo de plantilla sin reemplazar? → no se entrega así.

Si después de tachar quedan doce líneas, entrégalo con doce. Corto no es incompleto: corto es que
cada línea se lo ganó.
