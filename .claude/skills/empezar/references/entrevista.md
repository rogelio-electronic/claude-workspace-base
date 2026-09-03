# El guion de la entrevista

Objetivo de esta fase: salir con **el perfil, los límites y el tono** de una persona que no sabe
nada de Claude, en menos de cinco minutos y sin haberla hecho escribir párrafos.

Regla que manda sobre todo lo demás: **cada respuesta que ya tengas se salta**. Si en la pregunta
abierta te dijo "llevo la contabilidad de tres bodegas y todo está en Excel", ya no le preguntes con
qué archivos trabaja. Repreguntar lo obvio es la manera más rápida de que alguien decida que esto
no lo entiende.

---

## Antes de preguntar: mira la carpeta

Un `ls` y una ojeada. Si hay archivos, dicen más que tres preguntas: extensiones, nombres, idioma,
si hay un `.git`, si hay facturas o planos o código. Trae eso a la entrevista ya masticado
("veo que tienes doce Excel de nómina, ¿esto va por ahí?") — impresiona menos que preguntar y
sirve más.

---

## Pregunta abierta (en el chat, una sola)

> **¿Para qué vas a usar esta carpeta?** Cuéntamelo en dos o tres frases, como se lo contarías a un
> amigo. Sin tecnicismos, y no te preocupes por hacerlo bien: con lo que me digas yo armo el resto.

De esta respuesta sale casi todo: el oficio, el sector, el país si lo menciona, el idioma real, el
nivel de formalidad y —si se queja de algo— el primer candidato a skill. Escúchala entera antes de
lanzar la ronda 1.

Si contesta con una sola palabra ("trabajo"), no insistas: pasa a la ronda 1, que es de clics.

---

## Ronda 1 — cuatro preguntas (`AskUserQuestion`, todas juntas)

**1. `Trabajo` · ¿Qué vas a hacer aquí más seguido?** *(múltiple)*
- Escribir y revisar documentos — informes, propuestas, correos, actas
- Números, datos y reportes — Excel, cuentas, seguimiento, gráficos
- Organizar y decidir — planificar, hacer listas, comparar opciones, tomar decisiones
- Programar o automatizar — código, scripts, integrar herramientas

**2. `Archivos` · ¿Con qué trabajas normalmente?** *(múltiple)*
- Word, PDF, texto
- Excel, CSV, hojas de cálculo
- Código o archivos de configuración
- Casi nada guardado aquí: todo vive en la nube o en mi cabeza

**3. `Nivel` · ¿Qué tanto has usado herramientas como esta?** *(una)*
- Nunca. Explícame como si fuera nuevo en todo
- Lo básico. Uso apps, pero no programo
- Soy técnico. No me expliques lo obvio

**4. `Respuestas` · ¿Cómo prefieres que te conteste?** *(una)*
- Breve y al grano
- Explicado, con el porqué de las cosas
- Con todo el detalle técnico

---

## Ronda 2 — tres o cuatro preguntas (`AskUserQuestion`)

Las tres primeras son fijas. La cuarta la eliges tú según lo que ya sabes.

**1. `Límites` · ¿Hay algo que yo NO deba hacer sin preguntarte?** *(múltiple)*
- Nada especial, es una carpeta nueva
- No borres ni muevas archivos sin avisarme
- No mandes nada hacia afuera —correo, web, publicar— sin permiso
- Hay carpetas privadas aquí; te digo cuáles

**2. `Alcance` · ¿Esto es tuyo solo o lo va a usar más gente?** *(una)*
- Solo yo
- Mi equipo, y quiero que salga igual lo haga quien lo haga
- Es para un cliente o para entregar afuera

**3. `Idioma` · ¿En qué idioma trabajas?** *(una)*
- Español
- Inglés
- Los dos: te hablo en español, entrego en inglés

**4. La variable.** Elige *una* de estas según lo que marcó en la ronda 1:

| Si marcó… | Pregunta | Opciones |
|---|---|---|
| Números y datos | ¿De dónde salen esos datos? | Los lleno yo a mano · Los exporto de un sistema · Me los pasa otra persona · Todavía no sé |
| Documentos | ¿Tienes ya un formato o modelo que sigues? | Sí, tengo ejemplos que te puedo mostrar · Sí, pero está en mi cabeza · No, y me gustaría uno · Cada vez es distinto |
| Programar | ¿Cómo es el proyecto? | Ya existe y lo mantengo · Lo empiezo de cero · Son scripts sueltos · Es para automatizar cosas de oficina |
| Organizar | ¿Qué te está costando más hoy? | Perder el hilo de lo pendiente · Decidir entre opciones · Que todo esté en lugares distintos · Escribir lo que ya decidí |
| Nada claro | ¿Qué te haría decir "valió la pena"? | Ahorrarme horas repetidas · Que las cosas salgan más parejas · Entender algo que no entiendo · Todavía estoy explorando |

Si te faltó un dato importante y solo uno, pregúntalo suelto en el chat después. Una pregunta suelta
se perdona; una cuarta ronda de formulario, no.

---

## Qué inferir (no preguntar)

| Respuesta | Lo que se deduce y va al `CLAUDE.md` |
|---|---|
| "Nunca lo he usado" | Tono didáctico, confirmar antes de cada acción que cambie archivos, nunca mostrar comandos sin explicar qué hacen |
| "Soy técnico" | Ir al grano, mostrar comandos y rutas, saltarse las confirmaciones de cortesía |
| "Breve y al grano" | Respuestas cortas por defecto, sin resúmenes de lo que acaba de hacer |
| "Mi equipo lo va a usar" | Las skills deben quedar **repartibles**: nada de atajos que solo entienda quien las escribió |
| "Es para un cliente" | Los entregables mandan: formato, marca y tono se vuelven guardarraíles duros |
| "Hay carpetas privadas" | Va al `CLAUDE.md` como límite explícito y al `deny` de `.claude/settings.json` |
| Menciona un país | Moneda, impuestos, formato de fecha, feriados y normativa local — dato duro, va escrito |
| Se queja de algo ("siempre pierdo tiempo en…") | Primer candidato a skill. Tráelo textual a la fase 3 |
| Todo en la nube | No armes estructura de carpetas: arma el flujo de "pegar aquí → sale allá" |

---

## Errores que arruinan la entrevista

- **Preguntar lo técnico.** "¿Quieres que configure un hook?" es la respuesta equivocada a todo.
- **Más de tres rondas.** Después de la tercera, la calidad de las respuestas cae en picada.
- **Aceptar "lo que tú creas" como respuesta y quedarse callado.** Ahí conviene proponer: "por lo
  que me contaste haría X, ¿te sirve?" — y esperar solo un sí o un no.
- **Anotar todo.** No todo lo que dijo va al `CLAUDE.md`. Solo lo que cambia lo que Claude haría.
