# Problemas frecuentes

## Conexión y servidores

| Síntoma | Causa | Solución |
|---|---|---|
| MCP BUILDER dice **"offline"** | Claude Code está cerrado; el servidor HTTP `127.0.0.1:54321` lo levanta Claude Code | Abra Claude Code. El file-bridge sigue funcionando mientras tanto |
| El puerto 54321 parece ocupado | Otro proceso, normalmente un servidor MCP de otro chat, lo tiene tomado | `netstat -ano \| findstr 54321` y revise el PID |
| Tras actualizar el MCP **no aparecen** las herramientas nuevas (`/mcp` sigue mostrando 61 en vez de 111) | Los servidores MCP que ya estaban en marcha siguen con el código anterior; cerrar la ventana no los reinicia | **Cierre la app de Claude por completo**: clic derecho en el icono de la bandeja → **Quit**. Vuelva a abrirla y compruebe que hay un solo proceso `packet_tracer_mcp` con hora posterior a la instalación (vea [Actualización](actualizacion-y-vuelta-atras.md)) |
| Respuestas raras o cruzadas, comandos que "no llegan" | **Varios chats de Claude conectados a Packet Tracer a la vez**: cada chat arranca su propio servidor MCP y compiten por el puerto y por el file-bridge | Trabaje con **un solo chat de Claude conectado a Packet Tracer a la vez**. Cierre los demás chats o la app entera |
| Packet Tracer no responde a la IA, o el Wizard "no está abierto" aunque usted lo ve | **Dos procesos de Packet Tracer**, uno de ellos sin ventana (queda colgado en segundo plano) | Cierre el sobrante desde el Administrador de tareas: pestaña Detalles, `PacketTracer.exe`. Deje uno solo |
| Error `unknown option '-m'` al registrar el MCP | En PowerShell, `--` sin comillas | Use `"--"` entre comillas (vea [Instalación en Windows](instalacion-windows.md)) |
| `externally-managed-environment` al instalar en macOS | Python de Homebrew | Use el Python de python.org |

## Diálogos de Packet Tracer

| Síntoma | Causa | Solución |
|---|---|---|
| La IA dice "Packet Tracer has a dialog open (…)" y no envía nada | Hay un diálogo modal abierto. El MCP no envía órdenes detrás de un modal porque eso puede colgar Packet Tracer | Ciérrelo usted y avise. **No responda "Yes" a "Reset Network?"**: borraría lo configurado |
| Aparece **"Reset Network?"** | Visto una vez después de `pt_activity_check(refresh=True)` | Responda **No**. Tras un cambio por CLI use `refresh=False` |
| Aparece **"Use as the Answer Network?"** | Se abrió el Activity Wizard sobre un `.pkt` | Responda **Yes**. El script `importar_red_inicial.py` lo hace solo |
| `pt_send_raw` da *timeout* al abrir el Wizard | `fileActivityWizard()` queda esperando el diálogo anterior | Envíelo con `wait_result=False` y deje que el script responda el diálogo |

## Actividades (.pka)

| Síntoma | Causa | Solución |
|---|---|---|
| El estudiante abre una **pantalla en blanco** | La red inicial del `.pka` está vacía (0 equipos) | Importe la red inicial en el Wizard. Compruebe con `getInitNetworkFile().getMainNetwork().getDeviceCount()` |
| `pt_query_topology` o `ipc.network()` dan **0 equipos** con un `.pka` abierto | Con un `.pka` abierto esas vías no ven las redes de la actividad | Use `getInitNetworkFile()`, `getAnsNetworkFile()` o `getUserNetworkFile()` y luego `.getMainNetwork().getDeviceCount()` |
| El porcentaje inicial no es 0 % | Hay hojas que ya son correctas en la red inicial (por ejemplo `VTY Line 0/15 > Login` en un 2960) | Quítelas del checklist (vea [Checklist](checklist-activity-wizard.md)) |
| Una hoja aparece como faltante al marcar | La ruta no existe con ese nombre exacto | `pt_activity_tree(path)` para ver los nombres reales |
| Tras abrir un `.pka`, los contadores no cambian | Packet Tracer no recalcula hasta que la red cambia | Haga cualquier cambio real o use `pt_activity_check` después de configurar |
| `pt_activity_open` dice "The Activity Wizard is open" | Hay un Wizard abierto | `pt_activity_exit_wizard` (descarta lo no guardado) |
| Un `.pka` con contraseña queda bloqueado | La API exige la contraseña de autor | Ponga la contraseña **al final**, después de todas las pruebas |

## Prueba del estudiante

| Síntoma | Causa | Solución |
|---|---|---|
| El primer ping falla y el segundo funciona | El puerto tarda en pasar a reenvío (STP) y la primera solicitud ARP se pierde | Es normal: repítalo. Inclúyalo como consejo en el enunciado |
| El estudiante simulado llega al 100 % "demasiado fácil" | Puede estar construyendo desde cero sobre una red inicial vacía | Compruebe la red inicial (12 equipos en la 3.3) |

## Trabajo con Claude Code

- **No abra Claude Code dentro de este repositorio** para trabajar prácticas: se pone a revisar el código. Use una carpeta de trabajo aparte.
- Para no aprobar cada herramienta: `/permissions` → *Allow* → `mcp__packet-tracer`.
