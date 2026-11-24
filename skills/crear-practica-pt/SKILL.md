---
name: crear-practica-pt
description: >-
  Crea una práctica evaluable de Cisco Packet Tracer (.pka con checklist del Activity Wizard)
  a partir de una descripción, por ejemplo "variación de la 3.4 Configure Trunks": diseño
  original, red de respuesta e inicial, enunciado, solucionario, instrucciones HTML, checklist
  por API (pt_activity_*), verificación de 0 % inicial y prueba del estudiante con un subagente.
  Úsela cuando el docente pida crear, convertir o validar una práctica o actividad .pka de
  Redes II / CCNA. Trabaja junto con la skill packet-tracer (que enseña las herramientas);
  esta enseña el proceso.
---

# Crear una práctica evaluable de Packet Tracer

Uso: `/crear-practica-pt <descripción>`. Ejemplo: `/crear-practica-pt variación de la 3.4 Configure Trunks`.

Antes de usar cualquier herramienta `pt_*`, cargue la skill **packet-tracer**: tiene el catálogo de herramientas y la API exacta. Esta skill no la repite. Responda en español y trate al docente de "usted".

## Reglas que no se negocian

- **No invente** funciones, botones ni comandos. Si algo no está verificado aquí o en la skill packet-tracer, dígalo y márquelo como "no probado".
- **Nunca modifique** carpetas de prácticas existentes (`Prueba_<n>` ya creadas). Para probar algo, trabaje sobre copias.
- **Nunca guarde soluciones en un repositorio Git** (`.pka`, `.pkt`, solucionarios, `Config\`, contraseñas).
- **Un solo Packet Tracer** abierto y **un solo chat** conectado al MCP.
- Requiere **packet-tracer-mcp ≥ 0.12** (herramientas `pt_activity_*`). Si no están, deténgase y remita a la guía de actualización.
- Pausas **solo** donde un humano es imprescindible (marcadas con ⏸).

## Fase 0: Preparación

1. Pregunte o deduzca el número `<n>` y cree `Pruebas-PT\Prueba_<n>\` con la estructura de [reference/estructura-practica.md](reference/estructura-practica.md).
2. `pt_bridge_status` debe dar CONNECTED. Compruebe que existen `pt_activity_mark`, `pt_activity_save` y `pt_activity_set_instructions`.

## Fase 1: Diseño ⏸

Proponga un escenario **original**: no copie la actividad de Cisco. Cambie la topología, los nombres, las VLANs, el direccionamiento, los puertos, los hostnames y la contraseña. Entregue:

- Escenario en dos o tres frases.
- Tabla de equipos (modelos reales según `pt_list_devices`).
- Tabla de VLANs, de puertos y de IPs.
- Contraseña de la práctica.
- Qué traerá la red inicial y qué debe configurar el estudiante.
- Lista preliminar de lo que se calificará, aplicando [reference/reglas-checklist.md](reference/reglas-checklist.md).

**⏸ Pausa: espere la aprobación del docente.**

## Fase 2: Construcción

1. **Red de respuesta** con las herramientas del MCP (`pt_full_build` o `pt_plan_topology` → `pt_validate_plan` → `pt_live_deploy`, y luego `pt_cli` / `pt_host_ip_config`). Guárdela en `Test_1\Practica_<x>_Respuesta.pkt` con `pt_save_project`.
2. **Red inicial:** la misma topología, con solo lo que se entrega ya hecho. Guárdela en `Test_1\Practica_<x>_Inicial.pkt`.
3. **Enunciado** (`Enunciados\01_Enunciado_Estudiante.md`, plantilla en el repositorio: `templates/enunciado.md`):
   - Todo lo calificable, pedido **explícitamente**, sin comandos de la solución.
   - El archivo de trabajo es la actividad `.pka`.
   - Incluya el consejo de repetir el primer ping tras cambiar un puerto de VLAN.
4. **Solucionario** (`Enunciados\02_Solucionario_Docente.md`) y **scripts** (`Config\config_<hostname>.txt`).
5. **Instrucciones:** `Indicaciones\instrucciones_unificada.html`, en **una sola página** con `<style>` (base: [reference/plantilla-instrucciones.html](reference/plantilla-instrucciones.html)).
6. **Plan del checklist:** `Test_Final\checklist_plan.json` con las rutas de [reference/rutas-hojas.md](reference/rutas-hojas.md).
   - Excluya lo que ya es correcto en la red inicial.
   - Anote aparte los requisitos no calificables.

## Fase 3: Auditoría

Audite la red de respuesta con [reference/prompt-auditoria.md](reference/prompt-auditoria.md). Corrija y vuelva a auditar hasta que todo esté OK.

## Fase 4: Actividad y red inicial

1. `pt_open_project` con `Test_1\Practica_<x>_Respuesta.pkt`.
2. `pt_send_raw("ipc.appWindow().fileActivityWizard();", wait_result=False)`. **No espere el resultado:** Packet Tracer abre el diálogo "Use as the Answer Network?".
3. **Solo Windows:** ejecute el script de esta skill:
   ```text
   python "<carpeta de la skill>/scripts/importar_red_inicial.py" "<ruta absoluta>\Test_1\Practica_<x>_Inicial.pkt"
   ```
   El script responde *Yes*, pulsa **Import File to Initial Network**, elige el archivo y vuelve a Answer Network. Si imprime `"ok": true`, siga.
4. **⏸ Solo si el script falla, o en macOS:** pida al docente que haga lo mismo a mano.
   - Extensions → Activity Wizard (responder *Yes* si pregunta).
   - Initial Network → Import File to Initial Network → el `.pkt` inicial.
   - Volver a Answer Network **sin tocar casillas**.
5. Verifique con [reference/verificacion-js.md](reference/verificacion-js.md): Wizard abierto y red inicial con **más de 0 equipos**. Si da 0, deténgase.

## Fase 5: Checklist

1. `pt_activity_set_instructions(html)` con el HTML unificado. Debe responder `html_preserved: true` e `identical: true`.
2. `pt_activity_mark(rutas, clear_others=True)`. Debe dar `marked == N` y `missing: []`. Compruebe items == árbol == N **antes de guardar**.
3. `pt_activity_save("<ruta>\Test_Final\Prueba_<x>.pka")` → `pt_activity_exit_wizard` → `pt_activity_open(misma ruta)`.
4. Verifique tras reabrir:
   - items == árbol == N;
   - red inicial > 0 equipos;
   - instrucciones presentes;
   - **porcentaje inicial = 0 %**.
5. **Si el porcentaje inicial no es 0 %:**
   1. Identifique con `pt_activity_check(refresh=False, only_incorrect=False)` las hojas que ya dan *Correct*.
   2. Quítelas del plan.
   3. Reabra el Wizard sobre el `.pka` con `fileActivityWizard()`, marque de nuevo, guarde y verifique.

## Fase 6: Prueba del estudiante

1. Cree `prueba_estudiante\` con **solo** una copia del enunciado y una copia del `.pka`.
2. Lance un subagente sin contexto con [reference/prompt-estudiante.md](reference/prompt-estudiante.md).
3. Cuando termine, lea el resultado con `pt_activity_check(refresh=False)`. La meta es **100 %**.
4. Si no llega:
   - Diagnostique con las hojas incorrectas.
   - Corrija el enunciado, la red o el plan, sin reintentar a ciegas.
   - Repita la prueba con una copia nueva.

## Fase 7: Reporte

Escriba `reporte.md` (plantilla en el repositorio: `templates/reporte.md`) con:

- tabla de resultados (N ítems, red inicial, 0 %, % del estudiante);
- ítems no calificables;
- ambigüedades encontradas y si se corrigieron;
- **pasos manuales pendientes del docente** en el Wizard:
  - **Points** (en macOS no hay otra opción: cada ítem vale 1);
  - **Connectivity Tests** (en macOS el PKA Builder no los crea);
  - **contraseña de autor**, al final de todo.

## macOS

**No probado** con este flujo. Según el CHANGELOG 0.12 del proyecto original:

- el PKA Builder **no asigna puntos** ni **crea Connectivity Tests**;
- las instrucciones HTML necesitan `PT_UI_ALLOW_FOREGROUND=1` (sin ella se guardan como texto plano);
- el script de importación es solo para Windows.

La Mac del docente tiene Packet Tracer 9.0.0.0810; el autor del MCP verificó 9.0.1.
