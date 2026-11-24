# Petición de auditoría de la red de respuesta

Úsela en la Fase 3, con `Test_1\Practica_<x>_Respuesta.pkt` abierto en Packet Tracer.

```text
Audita la red de respuesta abierta en Packet Tracer contra el enunciado
(Enunciados\01_Enunciado_Estudiante.md) y el solucionario
(Enunciados\02_Solucionario_Docente.md). NO corrijas nada todavía.

Para cada requisito del enunciado, consulta el valor real con las herramientas del MCP:
- pt_cli: show vlan brief, show interfaces trunk, show interfaces <puerto> switchport,
  show running-config (hostname, enable secret, line con 0, line vty 0 15).
- pt_host_command / pt_get_device_details: IP, máscara y gateway de cada host.
- pt_host_command: los pings que pide el enunciado (repite una vez el primero si falla,
  por la convergencia de STP/ARP).

Entrega una tabla: requisito | esperado | real | OK/FALLA.
Al final, lista:
1. Requisitos del enunciado que no tienen una hoja calificable (ausencias, mls qos trust cos,
   estados intermedios).
2. Diferencias entre el enunciado y el solucionario.
3. Valores que ya son correctos en la red inicial (no deben calificarse).
```
