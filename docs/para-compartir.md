# Pasarle esto a otra persona

La plantilla está pensada para repartirse. Estas son las formas, de menos a más técnica.

## Las tres formas

**1. Un ZIP.** Comprime la carpeta y mándala. Que la descomprima, la renombre como quiera, la abra
con Claude y escriba `empezar`. No necesita saber qué es Git.

**2. Clonar el repositorio.**

```bash
git clone <url-del-repo> mi-trabajo
cd mi-trabajo
claude
```

**3. Tu propia versión.** Si tu equipo repite un oficio —todos hacen informes con el mismo formato,
todos facturan igual— haz una copia, configúrala una vez bien, borra lo que sea solo tuyo, y reparte
**esa**. Es la diferencia entre dar una plantilla y dar una plantilla que ya sabe de qué va el
trabajo.

## Antes de repartir: qué quitar

| Archivo | Qué hacer |
|---|---|
| `.claude/estado.json` | **Bórralo** si la otra persona va a configurar lo suyo. Si dejas el tuyo, `empezar` cree que ya está configurado |
| `CLAUDE.md` | Déjalo solo si el oficio es el mismo. Si tiene tus clientes o tus cifras, restáuralo a la versión de la plantilla |
| `BITACORA.md` | Bórralo. Es tu historial de decisiones, no el suyo |
| `investigacion/` | Las investigaciones sí se comparten y ahorran horas. Revisa que no tengan datos de clientes |
| `.claude/respaldos/`, `.claude/cuarentena/` | Bórralos. Son tuyos |
| Tus carpetas de trabajo | Obvio, pero se olvida |

Comprobación rápida antes de mandarlo:

```bash
git status --ignored          # ¿se va a colar algo que no debería?
python3 .claude/skills/mantenimiento/scripts/inventario.py
```

## Historial propio

Si clonaste el repositorio, tu carpeta arrastra el historial de la plantilla. Para empezar limpio:

```bash
rm -rf .git
git init
git add -A
git commit -m "Mi workspace"
```

No es obligatorio. Sirve para que tus cambios sean tuyos y para poder deshacer cualquier cosa que
Claude toque. Si nunca has usado Git, esto último es la razón de peso: es el "deshacer" que no
depende de la memoria de nadie.

## Un workspace por frente de trabajo

Copiar la carpeta cuesta diez segundos, y mezclar dos negocios en una sola sale caro:

- Las instrucciones se vuelven genéricas para servir a los dos, y dejan de servir a ninguno.
- Las skills se disparan donde no toca, porque su descripción tuvo que abrirse para abarcar más.
- Y el riesgo de verdad: que datos de un frente terminen en un documento del otro.

Si un pedido cruza dos workspaces, la respuesta correcta es decirlo en voz alta y pedir permiso
antes de tocar el segundo. Nunca en silencio.

## Lo que la otra persona necesita saber

Tres frases y nada más:

1. Instala Claude Code (o abre la app de escritorio) — está en `docs/instalar-claude-code.md`.
2. Abre esta carpeta con Claude.
3. Escribe `empezar` y contesta.

Si le mandas más instrucciones que eso, la plantilla está fallando en lo único que prometía.
