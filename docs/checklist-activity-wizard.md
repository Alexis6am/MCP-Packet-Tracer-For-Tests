# Checklist del Activity Wizard por API

El *checklist* (los *assessment items*) es lo que Packet Tracer usa para calificar una actividad. Esta página explica el método oficial de este proyecto para armarlo con la IA, verificado el 24 de noviembre de 2026 con packet-tracer-mcp 0.12.0 en Windows.

## Conceptos

- El checklist **solo existe en un `.pka`**. Un `.pkt` no tiene red de respuesta ni árbol de evaluación: `isActivityFile()` devuelve `false` y `getComparatorTree` no existe.
- Un `.pka` contiene tres redes:
  - **Answer Network**: la red resuelta. Los valores esperados salen de ahí.
  - **Initial Network**: la red con la que empieza el estudiante.
  - La red de trabajo del estudiante.
- Cada hoja marcada del árbol (*Assessment Items*) vale 1 punto. La ponderación se cambia a mano en la columna **Points**.
- La verdad es **`f.getAssessmentItemsCount()`**. `getCheckLeafCount()` y las palomitas del Wizard sirven para comparar, pero solas no prueban nada.

## Método oficial (MCP ≥ 0.12)

| # | Quién | Acción | Verificación |
|---|---|---|---|
| 1 | IA | Abre la red de respuesta (`pt_open_project`) y el Wizard (`aw.fileActivityWizard()` con `pt_send_raw`, sin esperar resultado). Packet Tracer pregunta "Use as the Answer Network?" | — |
| 2 | IA (script) o usted | El script `importar_red_inicial.py` de la skill responde *Yes*, pulsa **Import File to Initial Network**, elige el `.pkt` inicial y vuelve a Answer Network. Si falla, usted hace lo mismo a mano | Red inicial con equipos (> 0) |
| 3 | IA | `pt_activity_set_instructions` con **una sola página** HTML unificada | `html_preserved: true`, `identical: true` |
| 4 | IA | `pt_activity_mark(items, clear_others=True)` con la lista de rutas aprobada | `marked == N`, `missing: []`; items == árbol == N **antes de guardar** |
| 5 | IA | `pt_activity_save(ruta.pka)` → `pt_activity_exit_wizard` → `pt_activity_open(ruta.pka)` | Tras reabrir: items == árbol == N, red inicial > 0 equipos, **0 % inicial** |
| 6 | IA | Prueba del estudiante (vea [Validación](validacion-practica.md)) | 100 % |
| 7 | Usted | En el Wizard: Points, Connectivity Tests y contraseña de autor | — |

### Por qué funciona sin clics

`pt_activity_mark` hace `setCheck(true)` en **toda la cadena**: raíz → equipo → … → hoja. Con eso la hoja cuenta como ítem sin ningún clic humano. Marcar la raíz y el equipo **por API** no arrastra a sus demás hojas: con 3 rutas el conteo fue 3, y con 38 fue 38.

El método anterior marcaba **solo la hoja**, y esa hoja no contaba si el usuario no había hecho antes un clic en su casilla o en la de un antecesor. Por eso exigía un clic humano por equipo. Ese método está **superado en la v0.12** (vea la [bitácora](bitacora.md)).

### Guardado

`pt_activity_save` usa `fileSaveAsNoPrompt` y conserva las marcas, la red inicial importada y las instrucciones. La regla anterior de "guardar siempre con el botón Save del Wizard; Ctrl+S pierde el checklist" venía de marcas que nunca se habían registrado. También está **superada en la v0.12**.

Guardar con el botón Save del Wizard sigue siendo válido si usted trabaja a mano. Recuerde que **Exit** del Wizard advierte "Exiting the Activity Wizard will give you a new workspace. All unsaved settings will be lost": guarde antes de salir.

## Reglas para elegir las hojas

1. **Todo lo calificado debe pedirse EXPLÍCITAMENTE en el enunciado.**
2. **No marque valores que ya son correctos en la red inicial**, y **verifique siempre que el porcentaje inicial sea 0 %**. Ejemplo: en un 2960 de fábrica, `VTY Line 0 > Login` y `VTY Line 15 > Login` ya son correctos, porque el switch trae `login` en las líneas VTY. En la práctica 3.3 eso regalaba 4 puntos (9,5 % inicial); sin esas hojas el porcentaje inicial bajó a 0 %.
3. **No marque lo que ya viene en la red inicial**: cableado, troncales ya configurados, IPs ya dadas.
4. **Nunca deje marcados nodos padre ni "Network" a mano** en el Wizard: un clic en un padre marca cientos de hojas (MACs, puertos sin usar, STP…). `pt_activity_mark` con `clear_others=True` deja solo la lista.
5. **Rangos de líneas** (`line vty 0 15`): marque la primera y la última línea del rango (`VTY Line 0` y `VTY Line 15`), cada una con su `Password`. Su `Login` solo se marca si no viene ya correcto (regla 2).
6. **Listas** (por ejemplo, VLANs permitidas en un troncal): una hoja por elemento.
7. **Contraseñas:** Packet Tracer **sí** las valida aunque se vean cifradas (Enable Secret, Enable Password, consola y VTY). Comprobado: con la correcta → *Correct*; con otra → *Incorrect*.
8. **"Startup Config"** es un número (102, 104…), no el contenido: no la marque.
9. Las casillas desmarcadas de equipos que no se califican (PCs con IP ya dada, teléfono, Power Distribution Device, Instruction, Resource) son normales.

## Lo que no se puede calificar con hojas

- **Requisitos de ausencia** ("la VLAN X no debe existir en SW3"). Cúbralos de forma indirecta, por ejemplo con las VLANs permitidas del troncal, o con Connectivity Tests.
- **`mls qos trust cos`**: no tiene hoja.
- **Estados intermedios**: solo cuenta el estado final. En la 3.3, PC-AUX-01 primero va en la VLAN 37 y luego en la 64; solo se califica la 64.
- **Pings**: se califican con **Connectivity Tests**, que se crean a mano en el Wizard. El PKA Builder puede crearlos en Windows, pero eso **no se probó** en este proyecto.

## Rutas de hojas conocidas (switch 2960 y PC-PT)

| Requisito | Ruta | Valor en la red de respuesta |
|---|---|---|
| Hostname | `SWx > Host Name` | el hostname |
| enable secret | `SWx > Enable Secret` | hash MD5 (Packet Tracer usa una sal fija) |
| Consola | `SWx > Console Line > Password` / `Login` | contraseña / `1` |
| VTY 0 15 | `SWx > VTY Lines > VTY Line 0` y `VTY Line 15` `> Password` / `Login` | contraseña / `1` |
| VLAN con nombre | `SWx > VLANS > VLAN 37 > VLAN Name` | el nombre |
| Modo access | `SWx > Ports > FastEthernet0/5 > Dynamic Mode` | `3` = access, `1` = de fábrica, `2` = trunk |
| Modo (otra variante) | `SWx > Ports > FastEthernet0/1 > Port Mode` | según la práctica |
| VLAN de acceso | `SWx > Ports > FastEthernet0/5 > Access VLAN` | número de VLAN |
| VLAN de voz | `SWx > Ports > FastEthernet0/18 > Voice VLAN` | número de VLAN |
| VLANs permitidas | `SWx > Ports > GigabitEthernet0/1 > Trunk VLANs > (cada hijo)` | una hoja por VLAN |
| Cableado | `SWx > Ports > <puerto> > Link to <equipo> > Connects to <puerto>` / `Type` | — |
| IP de una PC | `PC > Ports > FastEthernet0 > IP Address` / `Subnet Mask` | IP / máscara |
| Sin gateway | `PC > Default Gateway` | `0.0.0.0` |

Para explorar otras rutas use `pt_activity_tree(path)`. Los nodos de cable se llaman `Link to <equipo>`. La API **no** tiene `getName()`; use `getNodeName()` y `getNodeValue()`.

## Verificaciones por API

Envíelas con `pt_send_raw(..., wait_result=True)`, en una sola línea dentro de `try/catch`:

```javascript
// Conteo de ítems y árbol
var f = ipc.appWindow().getActiveFile();
reportResult(JSON.stringify({items: f.getAssessmentItemsCount(),
                             tree: f.getComparatorTree().getCheckLeafCount(),
                             percent: f.getPercentageComplete()}));

// Equipos de cada red del .pka (ipc.network() y pt_query_topology dan 0 con un .pka abierto)
reportResult(JSON.stringify({
  inicial:   f.getInitNetworkFile().getMainNetwork().getDeviceCount(),
  respuesta: f.getAnsNetworkFile().getMainNetwork().getDeviceCount(),
  usuario:   f.getUserNetworkFile().getMainNetwork().getDeviceCount()}));
```

- `getCheckOnlyTree()` **no** sirve para listar los ítems: en la 3.3 devolvió 330 hojas para 42 ítems.
- `pt_activity_check` muestra el valor esperado de cada hoja. Úselo solo como docente, **nunca** en la prueba del estudiante.
- Tras un cambio por CLI, `pt_activity_check(refresh=False)` ya ve la nota nueva. Una vez, `refresh=True` fue seguido de un diálogo "Reset Network?" (vea [Problemas frecuentes](problemas-frecuentes.md)).

## Callejones sin salida (no repetir)

- Confiar en `root.getCheckLeafCount()` o en las palomitas como prueba de que el checklist se guardó.
- Creer que desplegar ramas del Wizard registra las hojas.
- Dejar marcado un nodo padre a mano para "refrescar": `SW2 > Ports` pasó de 23 a 956 hojas.
- Inventar métodos (`getName()`). Para listar los métodos de un objeto use `for (var k in obj)` dentro de `try/catch`.
- Descartar las contraseñas por el cifrado: el fallo inicial se debía a marcas no registradas, no al hash.

## Experimental / no probado

- `pt_activity_points` (puntos por API, solo Windows).
- Connectivity Tests creados por `pt_activity_create_exam`.
- Varias páginas de instrucciones por API. `pt_activity_set_instructions` escribe solo la primera, y por eso se usa una página unificada.
- `insertInstructionPage` por API.
