# Instalación en Windows

Esta guía deja listo un equipo Windows para crear prácticas evaluables con Claude Code y Packet Tracer. Todos los comandos se escriben en **PowerShell**.

Verificado en Windows 11 con Packet Tracer 9.0.0, packet-tracer-mcp 0.12.0 y la extensión `MCP-Control-Center.pts` de la release 0.12.0. El autor del MCP verificó el proyecto con Packet Tracer 9.0.1.

## 1. Python

1. Descargue Python 3.11 o superior desde <https://www.python.org/downloads/>.
2. En el instalador, marque **"Add python.exe to PATH"** antes de pulsar *Install Now*.
3. Compruebe la instalación en una ventana nueva de PowerShell:
   ```powershell
   python --version
   ```

## 2. Claude Code

1. Instálelo:
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
2. Ejecute `claude` e inicie sesión. Necesita un plan **Pro o superior**.

## 3. Servidor MCP de Packet Tracer

1. Instale el paquete con el extra `[ui]`. Ese extra instala `comtypes`, que el PKA Builder necesita para manejar la ventana del Activity Wizard:
   ```powershell
   pip install "packet-tracer-mcp[ui]"
   ```
2. Registre el servidor en Claude Code para todas sus carpetas:
   ```powershell
   claude mcp add --scope user --transport stdio packet-tracer "--" python -m packet_tracer_mcp --stdio
   ```
   Las comillas en `"--"` son **obligatorias en PowerShell**. Sin ellas aparece el error `unknown option '-m'`.
3. Compruebe la versión instalada:
   ```powershell
   pip show packet-tracer-mcp
   ```
   Este flujo necesita la **0.12.0 o superior**: es la primera versión con las herramientas `pt_activity_*`. Si actualiza desde una versión anterior, siga [Actualización y vuelta atrás](actualizacion-y-vuelta-atras.md).

## 4. Extensión de Packet Tracer

1. Descargue `MCP-Control-Center.pts` desde la página de *Releases* del proyecto original: <https://github.com/Mats2208/MCP-Packet-Tracer/releases>. En versiones anteriores el archivo se llamaba `V5.2.pts`.
2. En Packet Tracer: **Extensions → Scripting → Configure PT Script Modules → Add…** y elija el archivo `.pts`. Si había una versión anterior, quítela primero.
3. Reinicie Packet Tracer.
4. Abra la ventana de la extensión: **Extensions → MCP BUILDER**. La ventana se titula **"MCP Control Center"**.

En la ventana MCP Control Center:

- **"offline" con Claude Code cerrado es normal.** El servidor HTTP `127.0.0.1:54321` lo levanta Claude Code al arrancar.
- El canal **file-bridge** funciona siempre que Packet Tracer esté abierto con la extensión.
- El **token** se activa cuando se conecta el canal HTTP.
- Si sospecha que el puerto está ocupado:
  ```powershell
  netstat -ano | findstr 54321
  ```

## 5. Skills

Este proyecto usa dos skills que trabajan juntas:

| Skill | Qué enseña | Origen |
|---|---|---|
| `packet-tracer` | Las herramientas del MCP y la API de Packet Tracer | [`skill/`](../skill/SKILL.md) del proyecto original |
| `crear-practica-pt` | El proceso completo para crear una práctica evaluable | [`skills/crear-practica-pt/`](../skills/crear-practica-pt/README.md) de este fork |

1. Copie ambas carpetas (sustituya la ruta por la de su copia del repositorio):
   ```powershell
   Copy-Item -Recurse "C:\ruta\al\repo\skill" "$HOME\.claude\skills\packet-tracer"
   Copy-Item -Recurse "C:\ruta\al\repo\skills\crear-practica-pt" "$HOME\.claude\skills\crear-practica-pt"
   ```
2. En Claude Code ejecute `/reload-skills` y luego `/skills`.
3. Cada skill debe aparecer con **✓** y **sin** la marca "user-only". Si aparece `( )`, está desactivada: actívela.

## 6. Ajustes recomendados en Claude Code

- **Carpeta de trabajo aparte.** No abra Claude Code dentro de la carpeta de este repositorio para trabajar prácticas: se pone a revisar el código. Use una carpeta propia, por ejemplo `Pruebas-PT`.
- **Permisos.** En `/permissions` → *Allow*, agregue `mcp__packet-tracer` para no aprobar cada herramienta.
- **Modelo.** Con `/model`, use Sonnet para tareas normales y Opus para lo complejo (diseño, auditoría, diagnóstico).
- **Un solo chat conectado.** Trabaje con **un solo chat de Claude conectado a Packet Tracer a la vez** (vea [Problemas frecuentes](problemas-frecuentes.md)).

## 7. Comprobación final

Con Packet Tracer abierto y la ventana MCP BUILDER visible, pida en Claude Code:

```text
Comprueba pt_bridge_status y dime si existen las herramientas pt_activity_*.
```

La respuesta esperada es "CONNECTED" por HTTP y por file-bridge, y la presencia de las herramientas `pt_activity_*`.
