# Instalación en macOS

> **Estado: no probado de principio a fin.** Este flujo de prácticas solo se verificó en Windows 11. La Mac del docente tiene Packet Tracer **9.0.0.0810**, y con ella no se ha creado ninguna práctica completa. El autor del MCP verificó el proyecto original en macOS con Packet Tracer **9.0.1**. Trate cada paso de esta guía como **experimental**.

Todos los comandos se escriben en la aplicación **Terminal**.

## 1. Python

1. Descargue Python 3.11 o superior desde <https://www.python.org/downloads/>.
   - El `python3` que trae macOS es antiguo.
   - El Python de Homebrew puede rechazar `pip install` con el error `externally-managed-environment`.
2. Compruebe la versión:
   ```bash
   python3 --version
   ```

## 2. Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Después ejecute `claude` e inicie sesión. Necesita un plan Pro o superior.

## 3. Servidor MCP de Packet Tracer

1. Instale el paquete:
   ```bash
   python3 -m pip install packet-tracer-mcp
   ```
   El extra `[ui]` solo instala `comtypes`, que es para Windows. En macOS el PKA Builder maneja el Activity Wizard con el permiso de **Accesibilidad**, sin paquetes extra.
2. Registre el servidor:
   ```bash
   claude mcp add --scope user --transport stdio packet-tracer -- "$(command -v python3)" -m packet_tracer_mcp --stdio
   ```
3. Dé el permiso de Accesibilidad a la aplicación que ejecuta Claude Code (Terminal, o la app de Claude): **Ajustes del Sistema → Privacidad y seguridad → Accesibilidad**. Sin ese permiso, las herramientas del Wizard se niegan a funcionar y lo indican.

## 4. Extensión y skills

- **Extensión:** igual que en Windows. Descargue `MCP-Control-Center.pts` desde las *Releases* del proyecto original y cárguela con **Extensions → Scripting → Configure PT Script Modules → Add…**. El menú se llama **MCP BUILDER** y la ventana se titula "MCP Control Center".
- **Skills:**
  ```bash
  cp -R /ruta/al/repo/skill ~/.claude/skills/packet-tracer
  cp -R /ruta/al/repo/skills/crear-practica-pt ~/.claude/skills/crear-practica-pt
  ```
  Luego, en Claude Code, ejecute `/reload-skills` y `/skills`.

**Claude Code y Packet Tracer deben estar en el mismo sistema.** Si usa una máquina virtual (por ejemplo con UTM), instale ambos dentro de la VM.

## 5. Limitaciones de macOS (según el CHANGELOG de la 0.12.0 del proyecto original)

| Función | macOS |
|---|---|
| Abrir, calificar, marcar ítems y guardar `.pka` | Funciona según el autor |
| Crear la actividad con el Wizard | Funciona según el autor, con las limitaciones de abajo |
| **Puntos por ítem** (`pt_activity_points`) | **No disponible.** Cada ítem vale 1 punto; pondere a mano en la columna Points |
| **Connectivity Tests** | **No se crean**: se omiten con un aviso. Créelos a mano en el Wizard |
| **Instrucciones HTML** | Requieren la variable de entorno **`PT_UI_ALLOW_FOREGROUND=1`**. Sin ella, las instrucciones se guardan como **texto plano** |
| Calificar un `.pka` protegido con contraseña | La API rechaza la contraseña correcta: la actividad queda bloqueada |
| "Modo UI" (abrir y capturar ventanas de dispositivos) | Solo Windows |
| Importar la red inicial con el script de la skill | Solo Windows. En macOS hágalo a mano |

Con `PT_UI_ALLOW_FOREGROUND=1`, Packet Tracer pasa al frente unos segundos para importar el HTML. Lo hace cuando el teclado lleva 5 segundos sin uso. No escriba nada mientras tanto: lo que teclee caería en el diálogo de Packet Tracer.

Para pasar la variable al servidor, una opción es registrarlo con `-e` **(no probado en este proyecto)**:

```bash
claude mcp add --scope user --transport stdio -e PT_UI_ALLOW_FOREGROUND=1 packet-tracer -- "$(command -v python3)" -m packet_tracer_mcp --stdio
```

## 6. Comprobación

Con Packet Tracer abierto y la ventana MCP BUILDER visible, pida en Claude Code que compruebe `pt_bridge_status` y que existan las herramientas `pt_activity_*`.
