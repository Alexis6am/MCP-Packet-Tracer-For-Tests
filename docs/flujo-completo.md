# Flujo completo: crear una práctica evaluable

Este es el proceso oficial para convertir una idea ("variación de la 3.4 Configure Trunks") en una actividad `.pka` lista para entregar. La skill [`crear-practica-pt`](../skills/crear-practica-pt/README.md) lo sigue paso a paso; aquí se explica para que usted sepa qué ocurre y dónde intervenir.

## Antes de empezar

- Siga la [instalación](instalacion-windows.md) y compruebe que existen las herramientas `pt_activity_*` (MCP ≥ 0.12).
- Abra **un solo** Packet Tracer con la ventana **MCP BUILDER**, y **un solo** chat de Claude conectado.
- Trabaje en una carpeta propia, por ejemplo `Pruebas-PT`, **no** dentro de este repositorio.

## Estructura de cada práctica

Cada práctica vive en `Pruebas-PT\Prueba_<n>\`, fuera de Git:

```text
Prueba_<n>\
├── README.md                          indicaciones para el estudiante
├── Enunciados\
│   ├── 01_Enunciado_Estudiante.md
│   └── 02_Solucionario_Docente.md     ← contiene la solución: nunca a Git
├── Indicaciones\
│   └── instrucciones_unificada.html   una sola página para el Activity Wizard
├── Config\
│   └── config_<hostname>.txt          scripts de cada equipo ← solución
├── Test_1\
│   ├── Practica_<x>_Respuesta.pkt     red resuelta ← solución
│   └── Practica_<x>_Inicial.pkt       red con la que empieza el estudiante
├── Test_Final\
│   ├── checklist_plan.json            rutas de las hojas a calificar
│   └── Prueba_<x>.pka                 actividad del docente
├── prueba_estudiante\                 solo el enunciado y una copia del .pka
└── reporte.md
```

## Pasos

| # | Paso | Quién | Pausa |
|---|---|---|---|
| 0 | **Preparación:** crear la carpeta y comprobar `pt_bridge_status` | IA | — |
| 1 | **Diseño:** escenario original (no copiar a Cisco: cambiar topología, nombres, VLANs, direccionamiento, puertos, hostnames y contraseña) con su tabla de VLANs, puertos, IPs y contraseña | IA | **Sí: su aprobación** |
| 2 | **Construcción:** red de respuesta y red inicial (`.pkt`), enunciado (todo lo calificable pedido explícitamente, sin comandos), solucionario, scripts de configuración, instrucciones HTML unificadas y `checklist_plan.json` | IA | — |
| 3 | **Auditoría** de la red de respuesta contra el enunciado y el solucionario; corregir y volver a auditar hasta que todo esté OK | IA | — |
| 4 | **Actividad:** abrir la red de respuesta en el Activity Wizard e importar la red inicial | IA (script); si falla, usted | Solo si el script falla |
| 5 | **Checklist:** pegar las instrucciones, marcar las hojas, guardar, salir y reabrir; verificar items == árbol == N, red inicial con equipos y 0 % inicial | IA | — |
| 6 | **Prueba del estudiante** con un subagente sin contexto | IA | — |
| 7 | **Reporte** y pasos manuales: Points, Connectivity Tests y contraseña de autor | IA + usted | **Sí: sus pasos manuales** |

Detalles de cada paso:

- Pasos 4 y 5: [Checklist del Activity Wizard](checklist-activity-wizard.md).
- Instrucciones: [Instrucciones HTML](instrucciones-html.md).
- Pasos 3 y 6: [Validación de una práctica](validacion-practica.md).

## Paso 4 a mano (si el script falla)

1. Abra el `.pkt` de respuesta.
2. Vaya a **Extensions → Activity Wizard**. Si pregunta "Use as the Answer Network?", responda **Yes**.
3. Pase a **Initial Network → Import File to Initial Network** y elija el `.pkt` inicial.
   - Use *Copy from Answer Network* solo para pruebas: copia la solución completa.
4. Vuelva a **Answer Network** sin tocar ninguna casilla y avise a la IA.

> Una red inicial **vacía** hace que el estudiante abra una pantalla en blanco. La IA comprueba que la red inicial tenga equipos antes de marcar el checklist.

## Pasos manuales finales (en el Wizard)

1. **Points:** cada ítem vale 1 punto. Pondere en la columna Points si lo necesita.
2. **Connectivity Tests:** cree los pings que la práctica deba calificar.
3. **Contraseña de autor:** póngala **al final**, después de todas las pruebas. Con contraseña, la API queda bloqueada sin ella.
4. Guarde y vuelva a abrir el `.pka` para comprobar que todo se mantiene.
