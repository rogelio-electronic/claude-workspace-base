# Catálogo de perfiles

Mapa, no molde. Sirve para no empezar de cero y para no proponer tonterías. Si lo que te contaron no
encaja en ninguno, gana lo que te contaron.

Cada perfil trae tres cosas: las **carpetas** que suele usar de verdad, las **skills que aguantan**
el filtro (llevan dentro un dato que el modelo no puede adivinar) y las **skills que no** (suenan
bien, no sobreviven al primer mes).

---

## 1. Administración y oficina (PyME)

- **Carpetas:** `documentos/`, `plantillas/`, `proveedores/`, `entregables/`
- **Skills que aguantan:** redactar comunicaciones con el tono y la firma de la empresa · armar
  cotizaciones con el formato exacto que ya usan · minuta de reunión con las secciones del acta que
  entregan siempre
- **Skills que no:** "gestión de tiempo", "productividad", "redacción profesional"
- **Dato duro típico:** membrete, datos fiscales, condiciones comerciales estándar, nombres de los
  clientes recurrentes

## 2. Contabilidad y finanzas

- **Carpetas:** `movimientos/`, `conciliaciones/`, `reportes/`, `respaldos/`
- **Skills que aguantan:** conciliar extracto contra registro con las reglas del país · clasificar
  gastos con el catálogo de cuentas de esa empresa · cierre mensual con su checklist real
- **Skills que no:** "análisis financiero", "cómo hacer un balance"
- **Dato duro típico:** tasas de impuesto y fecha de vigencia, catálogo de cuentas, moneda y tipo de
  cambio que usan, tolerancia de diferencia aceptable
- **Ojo:** aquí el guardarraíl "ningún número sin documento de origen" no es opcional. Escríbelo.

## 3. Ventas y atención a clientes

- **Carpetas:** `clientes/`, `propuestas/`, `seguimiento/`
- **Skills que aguantan:** propuesta comercial con su estructura y su lista de precios · respuestas
  a objeciones frecuentes con el argumentario real · resumen semanal del pipeline
- **Skills que no:** "técnicas de venta", "escribir emails persuasivos"
- **Dato duro típico:** lista de precios y descuentos permitidos, segmentos de cliente, qué se puede
  prometer y qué no

## 4. Educación y docencia

- **Carpetas:** `clases/`, `evaluaciones/`, `materiales/`, `estudiantes/`
- **Skills que aguantan:** planificación de clase con el formato que exige la institución · rúbrica
  de evaluación con su escala real · retroalimentación con el tono que usa ese docente
- **Skills que no:** "pedagogía", "cómo enseñar mejor"
- **Dato duro típico:** currículo oficial, escala de calificación, formato institucional, edades

## 5. Ingeniería, obra y campo

- **Carpetas:** `proyectos/`, `informes/`, `mediciones/`, `fotos/`
- **Skills que aguantan:** informe de avance con las secciones que pide el cliente · valuación de
  obra con sus partidas · reporte de inspección contra la norma que aplica
- **Skills que no:** "gestión de proyectos", "buenas prácticas de ingeniería"
- **Dato duro típico:** normas aplicables y su versión, partidas y unidades, formato del cliente,
  criterios de aceptación

## 6. Programación y producto

- **Carpetas:** las del proyecto; no inventes estructura sobre un repo que ya existe
- **Skills que aguantan:** convenciones de ese repo que no están escritas · el ritual de despliegue ·
  formato de PR y de mensajes de commit del equipo
- **Skills que no:** "cómo programar en X", "buenas prácticas", "clean code" — el modelo ya sabe
  más de eso que cualquier skill que escribas
- **Dato duro típico:** comandos exactos de build y test, entornos, qué no se toca en producción
- **Ojo:** si hay un repo, lo primero es leerlo, no entrevistar. Y considera `/init` en vez de
  inventar un `CLAUDE.md` desde la conversación.

## 7. Investigación, tesis y academia

- **Carpetas:** `fuentes/`, `notas/`, `borradores/`, `figuras/`
- **Skills que aguantan:** citar en el estilo exacto que exige la revista o la universidad · fichar
  fuentes con los campos que después necesita · revisión de coherencia contra la pregunta de
  investigación
- **Skills que no:** "metodología de investigación", "cómo escribir académicamente"
- **Dato duro típico:** norma de citación y versión, estructura obligatoria, límite de palabras
- **Ojo:** guardarraíl innegociable — ninguna cita sin fuente verificable. Escríbelo.

## 8. Contenido y marketing

- **Carpetas:** `piezas/`, `referencias/`, `calendario/`
- **Skills que aguantan:** tono de voz de la marca **con ejemplos reales pegados dentro** · formatos
  por canal con sus límites de caracteres · brief creativo con su plantilla
- **Skills que no:** "copywriting", "storytelling", "SEO"
- **Dato duro típico:** tres a cinco piezas reales que sí sonaron a la marca, y una que no. Eso vale
  más que cualquier descripción del tono.

## 9. Legal

- **Carpetas:** `contratos/`, `modelos/`, `expedientes/`
- **Skills que aguantan:** cláusulas modelo de ese despacho · revisión de contrato contra su
  checklist de riesgos · formato de escrito según el tribunal
- **Skills que no:** "derecho contractual", "análisis legal"
- **Dato duro típico:** jurisdicción, modelos propios, qué cláusulas nunca se aceptan
- **Ojo:** guardarraíl obligatorio — esto asiste, no asesora; toda conclusión legal la revisa una
  persona antes de salir.

## 10. Salud y consultorio

- **Carpetas:** `pacientes/` (¡privada!), `protocolos/`, `documentos/`
- **Skills que aguantan:** formato de nota de evolución · consentimientos con su texto legal ·
  instrucciones al paciente en el tono del consultorio
- **Skills que no:** cualquier cosa que suene a diagnosticar
- **Ojo:** privacidad primero. `pacientes/` va al `.gitignore` y al `deny` de settings, y el
  `CLAUDE.md` dice explícitamente que nada de ahí sale de la máquina.

---

## Cuando no encaja en ninguno

Pregúntate solo esto: **¿qué entregable produce esta persona una y otra vez, y qué tendría que saber
Claude para que salga bien a la primera?** Eso es la skill. Todo lo demás es decorado.

Y si no produce un entregable repetido —está explorando, o cada semana hace algo distinto— entonces
la respuesta honesta es: **ninguna skill todavía**. Un `CLAUDE.md` bien escrito y las carpetas
ordenadas ya lo dejan mejor que al 90% de la gente. Díselo así, y ofrécele volver cuando aparezca la
primera tarea que repite.

---

## Carpetas: la regla corta

Crea una carpeta solo si se cumplen las dos: la persona la nombró o su perfil la usa siempre, **y**
va a tener algo dentro esta semana. Nada de `archivo/`, `varios/`, `pendientes/`. Las carpetas
vacías se llenan de nada y después nadie las borra.
