# Vía B — Adaptar una que ya existe

Para cuando el problema es común y alguien ya lo resolvió: revisar un PDF, escribir commits
decentes, armar una presentación, procesar un CSV. Buscar rinde. Instalar tal cual, no.

La regla de fondo, y la que casi nadie respeta: **lo bajado de internet muere primero**. No porque
esté mal escrito, sino porque estandariza *el proceso de otra persona*. Bájala por su dato duro y
tira su proceso.

---

## 1. Buscar

Necesitas internet en esta sesión. Si no lo tienes, dilo y ofrece la vía A o la C — no inventes
skills que "probablemente existen".

Dónde mirar, en este orden:

| Fuente | Qué esperar |
|---|---|
| `github.com/anthropics/skills` | Las oficiales de Anthropic. Bien escritas y mantenidas |
| Los plugins y marketplaces de Claude Code | Skills empaquetadas por dominio; a menudo hay una que ya trae lo que quieres |
| Buscar `claude skill <tema>` o `awesome claude skills` | Repos de la comunidad. Calidad muy dispar |
| El equipo de esa persona | Si alguien ya hizo el trabajo, no lo repitas |

Trae **dos o tres candidatas, no diez**, y preséntalas en una tabla de tres columnas: qué hace, qué
te llevarías de ahí, y qué le sobra para este caso.

## 2. Leerla antes de tocarla

Abre el `SKILL.md` completo y todo lo que traiga en `scripts/`. Sin excepción:

- **Un script que no leíste no se corre.** Punto. Ni para probar.
- Mira si asume rutas, cuentas, claves o herramientas que aquí no existen.
- Mira **de qué año es**. Una skill escrita para un modelo de hace dos años suele estar llena de
  andamiaje que hoy estorba más de lo que ayuda.
- Mira la licencia. Si la vas a adaptar y esta persona la va a repartir a su equipo, la atribución
  se respeta.

## 3. Quedarse con lo que sirve

De una skill ajena, lo valioso casi siempre es lo mismo, y casi nunca es el procedimiento:

**Sí sirve:** formatos concretos y plantillas de salida · listas de casos límite que alguien
descubrió a golpes · vocabulario y convenciones de un dominio · comandos exactos que funcionan ·
criterios de decisión bien pensados.

**No sirve:** su secuencia de pasos · sus recordatorios al modelo ("sé riguroso", "piensa paso a
paso") · sus ejemplos, que son de otro negocio · su tono · sus rutas.

Reescríbela entera para este workspace. Es más rápido de lo que parece y evita heredar los tics de
alguien que no conoces. Al terminar, aplícale el filtro de las tres R **a tu versión**: si al
quitarle los pasos ajenos no queda ningún dato duro, entonces esa skill nunca fue para esta persona.

## 4. Dejar dicho de dónde salió

En el cuerpo de la skill, una línea al final:

```markdown
> Adaptada de <nombre> (<URL>), consultada el <fecha>. Licencia <X>. Se conservó <qué>; se
> reescribió el resto para este workspace.
```

Y en `BITACORA.md`, la misma línea. Dentro de un año, cuando algo falle, la primera pregunta va a
ser de dónde salió esto.

---

## Guardarraíles de esta vía

- **Nunca la dejes tal cual**, ni "por ahora". El "por ahora" se queda dos años.
- **Ni credenciales, ni claves, ni endpoints ajenos.** Si la skill original pide una cuenta o una
  API, eso se decide aparte y con la persona delante.
- **Si viene de un plugin, no la edites en su sitio**: se pierde en la próxima actualización.
  Cópiala a `.claude/skills/` de este workspace y adapta ahí.
- **Una skill ajena sin dato duro no se adapta: se descarta.** Y se le dice a la persona que buscar
  no dio, que es un resultado perfectamente honesto.
