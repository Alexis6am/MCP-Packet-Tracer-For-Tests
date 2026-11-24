# Skill `crear-practica-pt`

Skill de Claude Code que guía el proceso completo para crear una práctica evaluable de Packet Tracer (actividad `.pka` con checklist), desde el diseño hasta la prueba del estudiante.

Trabaja **junto con** la skill `packet-tracer` del proyecto original:

- `packet-tracer` enseña las herramientas del MCP y la API de Packet Tracer;
- `crear-practica-pt` enseña el proceso.

Instale las dos.

## Requisitos

- packet-tracer-mcp **0.12.0 o superior**. En Windows, con el extra `[ui]`.
- Extensión `MCP-Control-Center.pts` cargada en Packet Tracer y la ventana **MCP BUILDER** abierta.
- Verificado en Windows 11 con Packet Tracer 9.0.0. **macOS: no probado** (vea [SKILL.md](SKILL.md)).

## Instalación

**Windows (PowerShell):**

```powershell
Copy-Item -Recurse "C:\ruta\al\repo\skills\crear-practica-pt" "$HOME\.claude\skills\crear-practica-pt"
Copy-Item -Recurse "C:\ruta\al\repo\skill" "$HOME\.claude\skills\packet-tracer"
```

**macOS (Terminal):**

```bash
cp -R /ruta/al/repo/skills/crear-practica-pt ~/.claude/skills/crear-practica-pt
cp -R /ruta/al/repo/skill ~/.claude/skills/packet-tracer
```

Luego, en Claude Code:

1. `/reload-skills`.
2. `/skills`: las dos deben aparecer con **✓** y sin "user-only".

## Uso

Abra Claude Code en su carpeta de prácticas (no en el repositorio) y escriba:

```text
/crear-practica-pt variación de la 3.4 Configure Trunks
```

## Contenido

| Archivo | Para qué |
|---|---|
| [`SKILL.md`](SKILL.md) | Las fases 0 a 7 y sus pausas |
| [`scripts/importar_red_inicial.py`](scripts/importar_red_inicial.py) | Importa la red inicial en el Activity Wizard por UI Automation (solo Windows) |
| [`reference/estructura-practica.md`](reference/estructura-practica.md) | Carpetas y archivos de cada práctica |
| [`reference/reglas-checklist.md`](reference/reglas-checklist.md) | Qué se marca y qué no |
| [`reference/rutas-hojas.md`](reference/rutas-hojas.md) | Rutas verificadas del árbol de evaluación |
| [`reference/verificacion-js.md`](reference/verificacion-js.md) | Comprobaciones por API |
| [`reference/prompt-auditoria.md`](reference/prompt-auditoria.md) | Petición para auditar la red de respuesta |
| [`reference/prompt-estudiante.md`](reference/prompt-estudiante.md) | Petición para la prueba del estudiante |
| [`reference/plantilla-instrucciones.html`](reference/plantilla-instrucciones.html) | Base de las instrucciones HTML |

Documentación completa: [flujo completo](../../docs/flujo-completo.md) y [checklist del Activity Wizard](../../docs/checklist-activity-wizard.md).
