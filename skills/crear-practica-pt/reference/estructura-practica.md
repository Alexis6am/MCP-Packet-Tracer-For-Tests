# Estructura de una práctica

Cada práctica vive en `Pruebas-PT\Prueba_<n>\`, **fuera de cualquier repositorio Git**.

```text
Prueba_<n>\
├── README.md                          indicaciones para el estudiante
├── Enunciados\
│   ├── 01_Enunciado_Estudiante.md
│   └── 02_Solucionario_Docente.md     SOLUCIÓN: no se entrega ni se versiona
├── Indicaciones\
│   └── instrucciones_unificada.html   una sola página, estilos en <style>
├── Config\
│   └── config_<hostname>.txt          scripts por equipo (SOLUCIÓN)
├── Test_1\
│   ├── Practica_<x>_Respuesta.pkt     red resuelta (SOLUCIÓN)
│   └── Practica_<x>_Inicial.pkt       red con la que empieza el estudiante
├── Test_Final\
│   ├── checklist_plan.json            rutas para pt_activity_mark
│   ├── Prueba_<x>.pka                 actividad del docente
│   └── Estudiante_<x>.pka             (opcional) copia resuelta por el estudiante simulado
├── prueba_estudiante\                 SOLO copia del enunciado + copia del .pka
└── reporte.md
```

- `<n>` es el número de carpeta (por ejemplo `Prueba_2`). `<x>` es el número de la actividad (por ejemplo `3.3`).
- No modifique carpetas `Prueba_<n>` ya existentes. Para experimentar, copie a una carpeta nueva con la misma estructura.
