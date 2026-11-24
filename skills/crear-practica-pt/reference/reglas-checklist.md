# Reglas del checklist (verificadas con MCP 0.12, Windows)

## Cómo se marca

- Use **`pt_activity_mark(rutas, clear_others=True)`**. Marca toda la cadena desde la raíz y las hojas cuentan como ítems **sin clics humanos**.
- **No** escriba `setCheck(true)` a mano solo en la hoja: en ese caso la hoja no cuenta si nadie hizo clic antes. Ese método está superado.
- La verdad es `f.getAssessmentItemsCount()`. Verifique **items == árbol == N** antes de guardar y otra vez **tras reabrir**.
- Guarde con `pt_activity_save`, salga con `pt_activity_exit_wizard` y reabra con `pt_activity_open`. Packet Tracer fija el árbol evaluado al cargar el archivo.

## Qué se marca

1. Solo lo que el enunciado pide **explícitamente**.
2. **Nada que ya sea correcto en la red inicial.** El **porcentaje inicial debe ser 0 %**. Ejemplo: en un 2960 de fábrica, `VTY Lines > VTY Line 0 > Login` y `VTY Line 15 > Login` ya son correctos; no se marcan.
3. Nada que ya venga en la red inicial: cableado, troncales configurados, IPs dadas.
4. **Rangos** (`line vty 0 15`): la primera y la última línea (`VTY Line 0`, `VTY Line 15`) con su `Password`.
5. **Listas** (VLANs permitidas): una hoja por elemento.
6. **Contraseñas:** sí. Packet Tracer valida Enable Secret, Enable Password, consola y VTY aunque se vean cifradas (correcta → *Correct*, otra → *Incorrect*).
7. Nunca nodos padre a mano ni "Network": un clic en un padre marca cientos de hojas.

## Qué no se puede calificar con hojas

- Requisitos de ausencia ("la VLAN X no debe existir"). Cúbralos con las VLANs permitidas del troncal o con Connectivity Tests.
- `mls qos trust cos` (no tiene hoja).
- Estados intermedios: solo cuenta el estado final.
- "Startup Config": es un número (102/104), no el contenido. No la marque.
- Pings: se califican con Connectivity Tests, que el docente crea a mano.

## Seguridad de la prueba

- `pt_activity_check` muestra los valores esperados: solo para el docente. **Nunca** en la prueba del estudiante.
- Tras un cambio por CLI use `pt_activity_check(refresh=False)`. Una vez `refresh=True` fue seguido de un diálogo "Reset Network?": hay que responder **No**.
- La contraseña de autor del `.pka` se pone **al final**: con ella la API queda bloqueada.
