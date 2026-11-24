# Bitácora del proyecto

Cronología de problemas y soluciones. Las fechas salen de los archivos de la carpeta de prácticas (`Pruebas-PT`) y de las notas de trabajo. Las prácticas y sus soluciones no están en este repositorio.

## 25 de octubre de 2026: Prueba 0, primer contacto

- Se instaló el MCP (versión 0.9.0) y se construyó una red de dos sucursales (`Prueba_0`) para comprobar que Claude Code controla Packet Tracer.
- Se verificó que el bridge conecta por HTTP y por file-bridge.

## 28–30 de octubre: Prueba 1, VLANs y troncales con 3 switches

- La IA escribió el enunciado, el solucionario y los scripts, y construyó la red de respuesta. La verificó con `show vlan brief`, `show interfaces trunk` y una matriz de pings.
- **Problema:** la IA marcaba hojas con `setCheck(true)` y el Wizard mostraba las palomitas, pero el archivo guardado solo tenía **2 ítems de 194**.
- **Diagnóstico:** una hoja marcada solo en la hoja únicamente contaba como ítem si el usuario había hecho antes un clic con el mouse en su casilla o en la de un antecesor. Desplegar ramas no bastaba. También se creyó que Ctrl+S perdía el checklist.
- **Solución de entonces ("método del clic"):**
  1. El humano hacía un clic en la casilla de cada equipo.
  2. La IA desmarcaba todo y marcaba la lista exacta.
  3. El humano guardaba con el botón Save del Wizard.
- Se guardaron versiones parciales de la actividad con porcentajes crecientes (44 %, 58 %, 74 %, 82 % y 100 %) para comprobar que el checklist calificaba bien.
- **Callejones sin salida:** confiar en las palomitas o en `getCheckLeafCount()`; dejar marcado un padre (`SW2 > Ports` pasó de 23 a 956 hojas); desmarcar y volver a marcar hojas nunca pulsadas (el conteo pasó de 27 a 0 y volvió a 27, sin cambiar el archivo); inventar métodos como `getName()`.

## 12 de noviembre: contraseñas y práctica 3.3

- **Contraseñas:** se comprobó que Packet Tracer **sí** valida Enable Secret, Enable Password, consola y VTY aunque se vean cifradas. El fallo inicial se debía a marcas no registradas, no al cifrado. Quedó documentado en la *Guía del checklist por API* (versión 2, PDF fuera del repositorio).
- **Práctica 3.3 (Clínica Valle Sereno):** VLANs 37, 48, 64 y 85, una VLAN de voz y un cambio de departamento. Actividad de 42 ítems con instrucciones HTML en 4 páginas.
- La prueba del estudiante dio 100 %. Más tarde se descubrió que ese resultado venía de construir la red **desde cero**: el `.pka` tenía la red inicial vacía (ver 24 de noviembre).
- El primer borrador del solucionario proponía calificar `mls qos trust cos`, "Startup Config" y `line vty 0 4` / `5 15`. Se corrigió: `mls qos trust cos` no tiene hoja, "Startup Config" es un número y las VTY se marcan como `VTY Line 0` y `VTY Line 15`.

## Fecha no registrada: modelos locales

Se probó Ollama con GLM-4.7-Flash y Qwen3.5-9B en una RTX 4070. Se descartó. Vea [Modelos locales](modelos-locales.md).

## 24 de noviembre: MCP 0.12 y PKA Builder

- **Actualización** de la 0.9.0 a la 0.12.0 con respaldo previo. Las herramientas nuevas no aparecían hasta **cerrar la app de Claude por completo**: los servidores MCP abiertos seguían con el código anterior.
- **Paso 0:** la copia del `.pka` de la 3.3 tenía 42 ítems, pero **0 equipos en la red inicial**. Se descubrió con `getInitNetworkFile().getMainNetwork().getDeviceCount()`, porque `pt_query_topology` devuelve 0 con cualquier `.pka`.
- **Mini-prueba 1:** sin ningún clic humano, `pt_activity_mark` marcó 3 hojas. Dio 3 ítems antes de guardar y 3 después de guardar con `pt_activity_save` y reabrir.
- **Mini-prueba 2:** con la red inicial importada a mano, el resultado se mantuvo y la red inicial (12 equipos) se conservó. El enable secret correcto dio *Correct*; uno distinto, *Incorrect*.
- **Ruta A:**
  1. Las 4 páginas de instrucciones se unificaron en una, que `pt_activity_set_instructions` pegó idéntica.
  2. Se marcaron 42 hojas: 42 antes de guardar y 42 tras reabrir.
  3. La prueba del estudiante con la red inicial real dio **42/42 = 100 %**.
- **v2:** las 4 hojas `VTY Line 0/15 > Login` ya eran correctas en la red inicial (9,5 % inicial). Sin ellas quedaron 38 ítems y **0 % inicial**. Nace la regla de verificar siempre el 0 % inicial.
- **Importación automática de la red inicial:**
  1. `aw.fileActivityWizard()` abre el Wizard sobre el archivo abierto.
  2. Un script con el driver de UI Automation del MCP responde "Use as the Answer Network?", pulsa *Import File to Initial Network* y elige el `.pkt` inicial.
  3. Se verificó en Windows: 12 equipos en la red inicial, con los valores del `.pkt` inicial.
- **Ambigüedades corregidas en la 3.3:** el enunciado decía que el archivo de trabajo era `.pkt` en vez de `.pka`, y faltaba el consejo de repetir el primer ping después de cambiar un puerto de VLAN.

### Superados en la v0.12

| Regla anterior | Por qué ya no aplica |
|---|---|
| "Un humano debe hacer un clic en la casilla de cada equipo antes de que la IA marque" (**método del clic**) | `pt_activity_mark` marca toda la cadena desde la raíz y las hojas cuentan sin clics |
| "Guardar siempre con el botón Save del Wizard; **Ctrl+S** pierde el checklist" | La confusión venía de marcas no registradas. `pt_activity_save` (`fileSaveAsNoPrompt`) conserva marcas, red inicial e instrucciones |
| "Pegar cada página de instrucciones a mano y volver a la página 1" | Se usa una sola página unificada y la pega `pt_activity_set_instructions` |
| "Importar la red inicial siempre a mano" | Lo hace el script `importar_red_inicial.py` en Windows; a mano solo si el script falla |
