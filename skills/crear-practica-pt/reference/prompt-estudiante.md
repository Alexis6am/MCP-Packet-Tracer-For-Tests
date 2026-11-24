# Petición para la prueba del estudiante

Lance un **subagente sin contexto** (herramienta Agent, tipo general-purpose) con este texto, después de crear `prueba_estudiante\` con **solo** una copia del enunciado y una copia del `.pka`. Es la versión que dio 42/42 = 100 % en la práctica 3.3. Reemplace las rutas.

```text
Eres un estudiante de Redes II resolviendo una práctica de Cisco Packet Tracer. Responde en español.

Tu ÚNICO material:
- El enunciado: <ruta>\prueba_estudiante\01_Enunciado_Estudiante.md
- La actividad: <ruta>\prueba_estudiante\Practica_<x>_estudiante.pka

Reglas estrictas:
- NO leas ningún otro archivo ni carpeta (nada de solucionarios, scripts, Config, Test_1,
  Test_Final, repositorios ni notas). Solo el enunciado.
- Packet Tracer ya está abierto y conectado mediante el MCP packet-tracer (cárgalas con
  ToolSearch: pt_activity_open, pt_cli, pt_host_ip_config, pt_host_command,
  pt_query_topology, pt_bridge_status).
- Primero abre la actividad con pt_activity_open(path=<la ruta del .pka>). Esa es la ÚNICA
  herramienta pt_activity_* que puedes usar. PROHIBIDO: pt_activity_check,
  pt_activity_status, pt_activity_tree, pt_activity_mark, pt_activity_save,
  pt_activity_reset, pt_activity_create*, pt_activity_points,
  pt_activity_set_instructions, pt_activity_build_initial, pt_activity_exit_wizard,
  pt_send_raw, pt_save_project, y cualquier herramienta que lea el checklist, la red de
  respuesta o guarde archivos.
- Configura solo lo que pide el enunciado, como lo haría un estudiante: CLI de los switches
  con pt_cli (usa el nombre del dispositivo en Packet Tracer aunque cambies el hostname),
  IP de PCs con pt_host_ip_config, pings con pt_host_command.
- No muevas ni cambies cables. NO guardes nada en disco.
- Si algo del enunciado es ambiguo, decide lo más razonable, sigue y anótalo.

Al terminar, entrega un informe breve:
1. Qué configuraste en cada equipo.
2. Resultados de los pings que pide el enunciado (esperado vs obtenido).
3. Lista de ambigüedades o dudas del enunciado (con la parte donde aparecen).
4. Problemas de herramientas.
No intentes calcular tu porcentaje.
```

Después, la IA principal lee el resultado con `pt_activity_check(refresh=False)`. La meta es 100 %.
