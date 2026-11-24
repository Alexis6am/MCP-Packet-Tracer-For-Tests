# Rutas de hojas conocidas

Verificadas en Packet Tracer 9.0.0 con switches 2960-24TT y PC-PT (prácticas 1 y 3.3). Úselas en `pt_activity_mark` como listas: `["SW-PB", "Ports", "FastEthernet0/5", "Access VLAN"]`.

| Requisito | Ruta | Valor esperado |
|---|---|---|
| Hostname | `SWx > Host Name` | hostname |
| enable secret | `SWx > Enable Secret` | hash MD5 (sal fija de Packet Tracer) |
| Consola: contraseña | `SWx > Console Line > Password` | contraseña |
| Consola: login | `SWx > Console Line > Login` | `1` |
| VTY: contraseña | `SWx > VTY Lines > VTY Line 0 > Password` y `VTY Line 15 > Password` | contraseña |
| VTY: login | `SWx > VTY Lines > VTY Line 0 > Login` y `VTY Line 15 > Login` | `1` (**ya correcto de fábrica en el 2960: no marcar**) |
| Nombre de VLAN | `SWx > VLANS > VLAN <n> > VLAN Name` | nombre |
| Modo access | `SWx > Ports > FastEthernet0/<n> > Dynamic Mode` | `3` access, `1` de fábrica, `2` trunk |
| Modo (variante) | `SWx > Ports > <puerto> > Port Mode` | según la práctica |
| VLAN de acceso | `SWx > Ports > FastEthernet0/<n> > Access VLAN` | número |
| VLAN de voz | `SWx > Ports > FastEthernet0/<n> > Voice VLAN` | número |
| VLANs permitidas | `SWx > Ports > GigabitEthernet0/1 > Trunk VLANs > (cada hijo)` | una hoja por VLAN |
| Cableado | `SWx > Ports > <puerto> > Link to <equipo> > Connects to <puerto>` / `Type` | — |
| IP de PC | `PC > Ports > FastEthernet0 > IP Address` / `Subnet Mask` | IP / máscara |
| Sin gateway | `PC > Default Gateway` | `0.0.0.0` |

## Cómo descubrir rutas nuevas

- `pt_activity_tree(["SW-PB"])`, luego `pt_activity_tree(["SW-PB", "Ports"])`, y así sucesivamente.
- Los nodos de cable se llaman `Link to <equipo>`.
- La API no tiene `getName()`: use `getNodeName()` y `getNodeValue()`.
- Una ruta que no existe aparece en `missing` de `pt_activity_mark`, con los nombres disponibles en ese nivel.

## Ejemplo: la 3.3 (38 hojas)

Por cada switch (SW-PB, SW-P1):

- Host Name y Enable Secret.
- Console Line: Password y Login.
- VTY Line 0 y VTY Line 15: Password.
- VLAN 37, 48, 64 y 85: VLAN Name.
- Por cada puerto de PC: Access VLAN y Dynamic Mode.

Además:

- SW-PB Fa0/18: Access VLAN, Voice VLAN y Dynamic Mode.
- PC-AUX-01: FastEthernet0 > IP Address.
