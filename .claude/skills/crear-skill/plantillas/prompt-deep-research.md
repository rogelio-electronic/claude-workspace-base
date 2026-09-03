# Plantilla del prompt de investigación profunda

Para Gemini (Deep Research), Perplexity (Research) o cualquier buscador profundo.

**No la entregues genérica.** La mitad de su valor está en el contexto que le metes: el país, el
sector, el cliente, la frase con la que esa persona describió su problema. Rellena todo lo que esté
entre `<>` y borra lo que no aplique.

Objetivo del prompt: que vuelva con **lo que un experto tiene en la cabeza y un manual no dice**.
No un tutorial, no una introducción al tema. Datos duros, verificables y fechados.

---

## La plantilla

````markdown
Necesito material para construir una guía operativa —no un tutorial— sobre:

**<TEMA, en una línea concreta. No "facturación": "facturación de servicios de
construcción a entes públicos en Venezuela".>**

## Quién la va a usar

- <Rol y sector: "administradora de una constructora pequeña">
- <Dónde: país, región, jurisdicción. Esto decide qué normas aplican>
- <Qué hace con esto en su día a día, en sus palabras>
- <Con qué trabaja: Excel, PDF, un sistema concreto>
- <Para quién es el resultado: cliente, jefe, ente público, uso interno>

## Qué necesito que investigues

Entrégalo en Markdown, con estas secciones y en este orden:

1. **Reglas duras.** Lo que no se deduce por sentido común: umbrales, límites legales,
   plazos, tolerancias, tasas, normas aplicables y su versión vigente. Cada una con su
   fuente y su fecha.
2. **Formatos exactos.** Cómo se ve un entregable bien hecho: estructura, secciones
   obligatorias, campos, nomenclatura. Transcribe ejemplos reales, no los describas.
3. **Criterios de decisión.** Cuándo se hace A y cuándo B, en tabla:
   situación → qué se hace → por qué.
4. **Errores caros.** Los diez más frecuentes en la práctica real, cada uno con la señal
   que lo delata *antes* de que sea tarde.
5. **Vocabulario.** De quince a veinticinco términos del oficio, con la definición que usa
   el gremio, no la del diccionario.
6. **Cómo se verifica.** Cómo sabe un profesional que el trabajo quedó bien: qué revisa,
   contra qué lo compara, qué checklist usa antes de entregar.
7. **Qué cambió recientemente.** Cualquier cosa que se haya movido en los últimos dos años,
   con la fecha del cambio.
8. **Fuentes.** Lista con URL y fecha de consulta, marcando cuáles son oficiales.

## Cómo quiero que investigues

- Prioriza fuentes primarias y oficiales de <país / sector>. Documentos normativos por
  encima de blogs.
- Fecha cada dato. Si una cifra o una norma cambió, dime desde cuándo rige la actual.
- **No me des pasos genéricos** ("primero abre el archivo", "organiza tu trabajo"). Dame lo
  específico: números, formatos, nombres, reglas.
- Si un dato no lo pudiste confirmar, márcalo **sin confirmar** en vez de rellenarlo.
- Si hay desacuerdo real entre fuentes, muéstrame las dos posiciones y quién sostiene cada una.
- Extensión: la que haga falta. Prefiero denso y verificable a largo y vago.
````

---

## Ajustes según el caso

Añade solo lo que aplique. Cada línea de más te devuelve páginas de más.

| Si el tema es… | Agrega esta línea |
|---|---|
| Legal, fiscal o contable | "Cita el artículo o la resolución exacta de cada regla, y su fecha de entrada en vigor." |
| Técnico o de ingeniería | "Indica la norma y su edición (por ejemplo ISO 9001:2015), no solo el número." |
| De formato o entregable | "Transcribe la estructura completa de al menos dos ejemplos reales publicados." |
| De un oficio con jerga | "Incluye cómo lo llama la gente en la práctica, no solo el término formal." |
| De herramientas o software | "Di qué versión, y advierte si algo cambió en los últimos dos años." |
| Sensible o con riesgo | "Marca explícitamente qué decisiones no debería tomar una máquina sin revisión humana." |

## Errores al escribir este prompt

- **Dejarlo genérico.** "Investiga sobre gestión de proyectos" devuelve una enciclopedia
  inservible. El contexto es lo que lo hace útil.
- **Pedirle el proceso.** No le pidas "cómo hacer X paso a paso": eso el modelo ya lo sabe y solo
  vas a tener que tirarlo después. Pídele los datos.
- **No pedir fuentes ni fechas.** Sin eso, la investigación no se puede auditar y en un año no vas
  a saber qué sigue vigente.
- **Pedir demasiado en un solo prompt.** Si el tema tiene dos partes muy distintas, son dos
  investigaciones. Salen mejor las dos.
