# Fase 2: qué se escribe

Cuatro cosas, en este orden. Nada más. Cada una tiene su límite y su razón de existir.

---

## 1. `CLAUDE.md` — el archivo caro

Se **reescribe completo**, no se parchea. Plantilla: `plantillas/CLAUDE-md.md`.

Es el único archivo de este workspace que Claude lee **entero, en cada sesión, para siempre**. Ese
es su precio. La vara para cada línea es una sola pregunta:

> **¿Claude haría algo distinto si esta línea no estuviera?**

Si la respuesta es no, la línea no va. Aplícala sin piedad, especialmente a estas, que son las que
siempre se cuelan:

| No escribas | Por qué |
|---|---|
| "Sé cuidadoso", "revisa bien", "no inventes datos" | Ya lo hace. Solo ocupa espacio |
| "Responde en español" si ya está escrito en español | Se deduce del propio archivo |
| Un resumen del proyecto que ya se ve en la carpeta | Lo va a leer cuando le haga falta |
| La lista de skills instaladas | Claude ya las ve; se desactualiza sola |
| Historia, contexto emocional, agradecimientos | No cambia ninguna decisión |
| Procedimientos de doce pasos | Eso es una skill, o no es nada |

**Sí escribe:** qué es este workspace en una línea · a qué se dedica la persona y para quién trabaja
· los límites duros (lo que no se toca, lo que no sale de la máquina) · el idioma y el tono de
respuesta · dónde vive cada cosa, si la estructura no es evidente · las tres o cuatro reglas del
oficio que el modelo no puede adivinar (moneda, norma, formato del cliente, tolerancias).

**Presupuesto: cabe en una pantalla.** Cuarenta líneas es mucho. Veinte bien escritas es un buen
workspace. Si te pasas, casi siempre es porque metiste un procedimiento donde iba un límite.

Si la carpeta ya tenía un `CLAUDE.md` con contenido de la persona, respáldalo primero:

```bash
cp CLAUDE.md .claude/respaldos/CLAUDE.md.$(date +%Y-%m-%d-%H%M)
```

---

## 2. Las carpetas

Las que dijo la persona, o las de su perfil que va a usar esta semana. Ni una más.

```bash
mkdir -p documentos entregables   # ejemplo; ajusta al caso real
```

Nombres en el idioma de la persona, en minúsculas, sin espacios ni acentos si puedes evitarlos
(hacen ruido en la terminal). Si una carpeta necesita explicación, la explicación va en el
`CLAUDE.md`, no en un `LEEME.md` dentro de cada carpeta.

**Privacidad:** cualquier carpeta que la persona marcó como privada va a las tres partes —
`.gitignore`, el `deny` de `.claude/settings.json`, y una línea explícita en el `CLAUDE.md`.

---

## 3. `.claude/estado.json` — la memoria de la configuración

No lo escribas a mano. El script lo valida y lo formatea:

```bash
python3 .claude/skills/empezar/scripts/estado.py init \
  --resumen "Lleva la administración de una constructora pequeña en Venezuela" \
  --perfil administracion \
  --idioma es \
  --nivel basico \
  --estilo breve \
  --trabajo documentos,datos \
  --archivos word-pdf,excel \
  --limites "no borrar sin preguntar,no enviar nada afuera" \
  --compartido equipo \
  --carpetas documentos,entregables,proveedores
```

Para agregar skills pendientes o notas, después:

```bash
python3 .claude/skills/empezar/scripts/estado.py skill "cotizaciones" --via investigacion
python3 .claude/skills/empezar/scripts/estado.py nota "Trabaja en dólares, no en bolívares"
```

Este archivo existe para tres cosas: que `ayuda` sepa explicarle su propio workspace, que
`mantenimiento` sepa qué revisar y cuándo, y que si vuelve dentro de seis meses no haya que
entrevistarla otra vez. No es documentación: no metas ahí prosa.

---

## 4. `BITACORA.md` — la primera entrada

Plantilla: `plantillas/BITACORA.md`. Una entrada, corta, en el idioma de la persona: qué se
configuró, qué decidió, qué quedó pendiente y **cuándo toca revisar**.

La fecha de próxima revisión no es burocracia: toda configuración nace con caducidad, porque el
próximo modelo hace solo la mitad de lo que hoy le estás escribiendo. Tres meses por defecto, o el
próximo modelo nuevo, lo que llegue antes.

---

## Y antes de cantar victoria

```bash
python3 .claude/skills/empezar/scripts/estado.py verificar
```

Tiene que decir **PASA**. Si dice FALLA, arregla lo que enumera; no expliques el fallo, córrígelo y
vuelve a correrlo.

Después vienen las tres frases para copiar y la prueba en vivo. Sin eso, esto no está entregado:
está instalado, que no es lo mismo.
