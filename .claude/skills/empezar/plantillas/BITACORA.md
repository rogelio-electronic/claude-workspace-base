# La forma de la bitácora

Archivo `BITACORA.md` en la raíz del workspace. Se escribe en el idioma de la persona. Entradas
nuevas **arriba**, para que la última esté siempre a la vista.

Existe para responder, dentro de seis meses, una sola pregunta: *"¿por qué esto está configurado
así?"*. No es un diario ni un registro de todo lo que se hizo en la sesión.

---

## Forma de una entrada

```markdown
## 2026-09-02 — Configuración inicial

**Perfil:** administración de constructora pequeña, Venezuela. Entregables van al cliente.

**Se configuró:** CLAUDE.md con tono breve y límites de privacidad. Carpetas `valuaciones/`,
`proveedores/`, `entregables/`.

**Se decidió:**
- Todo en dólares; la conversión se anota con tasa y fecha. (Lo pidió él, es su regla contable.)
- `nomina/` queda fuera de todo: .gitignore, deny de settings y línea en CLAUDE.md.

**Pendiente:** skill de valuaciones — espera la investigación de Gemini en
`investigacion/valuaciones/`.

**Próxima revisión:** 2026-12-02, o cuando salga un modelo nuevo (lo que llegue antes).
```

---

## Qué entra y qué no

**Entra:** decisiones con su razón · lo que se apagó o se descartó y por qué · lo que quedó
pendiente y de qué depende · la fecha de próxima revisión · lo que falló de verdad en uso real (ese
es el único material con el que después se justifica devolver una instrucción).

**No entra:** la lista de archivos que creaste (se ve en la carpeta) · el contenido de la
conversación · felicitaciones · nada que se desactualice solo.

Tres a seis líneas por entrada. Si necesitas más, es que estás contando la sesión en vez de anotar
la decisión.
