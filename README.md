# Prácticas evaluables de Packet Tracer creadas con IA

Proyecto de prácticas preprofesionales de **Kevin Mendez** para la asignatura **Redes II** de la **Universidad Politécnica Salesiana (UPS)**.

Este repositorio es un *fork* de [Packet Tracer MCP](https://github.com/Mats2208/MCP-Packet-Tracer), de Mats2208. Ese proyecto conecta Claude Code con Cisco Packet Tracer 9. Aquí se usa para crear, con ayuda de la IA, **prácticas evaluables**: variaciones originales de las actividades de CCNA 2 (SRWE v7) que se entregan como actividades `.pka` con **calificación automática** (el *checklist* del Activity Wizard).

> El código del proyecto original (`src/`, `EXTENSION/`, `skill/`, `tests/`) no se modificó. Lo que agrega este fork es documentación en español, plantillas y la skill [`crear-practica-pt`](skills/crear-practica-pt/README.md).

## ¿Para qué sirve?

Usted describe la práctica que quiere ("una variación de la 3.4 Configure Trunks"). La IA diseña un escenario propio, construye la red en Packet Tracer, escribe el enunciado y el solucionario, arma el checklist y comprueba con un "estudiante simulado" que la práctica se puede resolver al 100 %.

| Paso | Quién lo hace | Resultado |
|---|---|---|
| 1. Diseño del escenario (topología, VLANs, direccionamiento, contraseñas) | IA, con **su aprobación** | Tabla de diseño |
| 2. Red de respuesta, red inicial, enunciado, solucionario, instrucciones HTML | IA | Archivos `.pkt`, `.md` y `.html` |
| 3. Auditoría de la red de respuesta contra el enunciado | IA | Tabla requisito / esperado / real |
| 4. Abrir el Activity Wizard e importar la red inicial | IA (script de UI Automation); si falla, **usted** | Actividad con red inicial |
| 5. Instrucciones, checklist, guardado y verificación (ítems = N, 0 % inicial) | IA (`pt_activity_*`) | Actividad `.pka` |
| 6. Prueba del estudiante (subagente sin contexto) | IA | Porcentaje obtenido (meta: 100 %) |
| 7. Puntos, pruebas de conectividad y contraseña de autor | **Usted**, en el Wizard | `.pka` lista para entregar |

El resultado real de la práctica 3.3 (VLANs, "Clínica Valle Sereno") fue de **42/42 ítems (100 %)** en la prueba del estudiante, con la red inicial real y sin ningún clic manual en el checklist. Vea la [bitácora](docs/bitacora.md).

## Inicio rápido (Windows)

1. Instale Python 3.11 o superior, Claude Code y el servidor MCP:
   ```powershell
   pip install "packet-tracer-mcp[ui]"
   claude mcp add --scope user --transport stdio packet-tracer "--" python -m packet_tracer_mcp --stdio
   ```
2. Cargue la extensión `MCP-Control-Center.pts` en Packet Tracer y abra **Extensions → MCP BUILDER**.
3. Copie las skills `packet-tracer` (de [`skill/`](skill/SKILL.md)) y [`crear-practica-pt`](skills/crear-practica-pt/README.md) a `~/.claude/skills/`.
4. Abra Claude Code en una carpeta de trabajo (no en este repositorio) y escriba:
   ```text
   /crear-practica-pt variación de la 3.4 Configure Trunks
   ```

Los pasos completos están en [Instalación en Windows](docs/instalacion-windows.md).

## Documentación

| Documento | Contenido |
|---|---|
| [Instalación en Windows](docs/instalacion-windows.md) | Python, Claude Code, MCP, extensión y skills, paso a paso |
| [Instalación en macOS](docs/instalacion-macos.md) | Igual para macOS (**no probado** de principio a fin) |
| [Actualización y vuelta atrás](docs/actualizacion-y-vuelta-atras.md) | Cómo pasar a una versión nueva del MCP sin perder la anterior |
| [Flujo completo](docs/flujo-completo.md) | El proceso oficial para crear una práctica evaluable |
| [Checklist del Activity Wizard](docs/checklist-activity-wizard.md) | Método por API, reglas, rutas de hojas y verificaciones |
| [Instrucciones HTML](docs/instrucciones-html.md) | Cómo escribir y pegar las instrucciones de la actividad |
| [Validación de una práctica](docs/validacion-practica.md) | Auditoría de la red y prueba del estudiante |
| [Problemas frecuentes](docs/problemas-frecuentes.md) | Síntomas, causas y soluciones |
| [Modelos locales](docs/modelos-locales.md) | Experimento con Ollama y por qué no se usa |
| [Bitácora](docs/bitacora.md) | Cronología de problemas y soluciones |
| [Proyecto original](docs/proyecto-original.md) | README original de Packet Tracer MCP (en inglés) |
| [Plantillas](templates/README.md) | Enunciado, solucionario, instrucciones, plan del checklist y reporte |

## Versiones probadas

| Componente | Versión |
|---|---|
| packet-tracer-mcp | 0.12.0 (con el extra `[ui]`) |
| Extensión | `MCP-Control-Center.pts` de la release 0.12.0 |
| Packet Tracer (Windows del docente) | 9.0.0 |
| Packet Tracer (verificado por el autor del MCP) | 9.0.1 |
| Packet Tracer (Mac del docente) | 9.0.0.0810, **no probado** con este flujo |
| Sistema operativo | Windows 11. macOS: **no probado** |

## Qué no se guarda en este repositorio

Las prácticas reales (actividades `.pka`, redes `.pkt`, solucionarios, scripts de configuración y contraseñas) se guardan **fuera de Git**, en una carpeta aparte (`Pruebas-PT`). El [`.gitignore`](.gitignore) excluye `*.pka`, `*.pkt` y las carpetas de prácticas.

## Créditos

- **Packet Tracer MCP**, de **Mats2208**: servidor MCP, extensión y skill `packet-tracer` en los que se basa todo este trabajo. Repositorio: <https://github.com/Mats2208/MCP-Packet-Tracer>. Licencia [MIT](LICENSE).
- **PTBuilder**, de **Kim Knight** ([@kimmknight](https://github.com/kimmknight)): <https://github.com/kimmknight/PTBuilder>. El proyecto original se inspiró en su lógica para el Script Engine de Packet Tracer (vea los [créditos del proyecto original](docs/credits.md)).
- **Antecedente:** Michelle Carolina Merchán Loja, *Manual Técnico y de Usuario: Cisco Packet Tracer Activity Wizard*, Universidad Politécnica Salesiana, marzo de 2026. Ese manual describe la creación manual de actividades con el Activity Wizard; este proyecto lo toma como referencia y automatiza el proceso con IA.
- Cisco, Packet Tracer, CCNA y Networking Academy son marcas de Cisco. Este proyecto no está afiliado a Cisco, y las prácticas que genera son escenarios propios, no contenido de Cisco.

Este fork mantiene la licencia [MIT](LICENSE) del proyecto original.
