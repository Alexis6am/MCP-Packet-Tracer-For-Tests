# Validación de una práctica

Antes de entregar una práctica se hacen dos comprobaciones independientes: la **auditoría** de la red de respuesta y la **prueba del estudiante**.

## 1. Auditoría de la red de respuesta

La IA revisa la red de respuesta (`Test_1\Practica_<x>_Respuesta.pkt`) contra el enunciado y el solucionario. Para cada requisito consulta la configuración real: `show vlan brief`, `show interfaces trunk`, `show interfaces <puerto> switchport`, `show running-config`, IPs de los hosts y pings.

El resultado es una tabla **sin correcciones** (primero se informa, después se corrige):

| Requisito | Esperado | Real | OK/FALLA |
|---|---|---|---|
| Hostname de SW-PB | `CVS-PB-SW` | `CVS-PB-SW` | OK |
| Fa0/18: VLAN de voz | 85 | 85 | OK |

Se corrige lo que falle y se vuelve a auditar hasta que todo esté OK. El texto de la petición está en la skill: `reference/prompt-auditoria.md`.

## 2. Prueba del estudiante

Un **subagente sin contexto** hace la práctica como si fuera un estudiante.

Condiciones:

- Carpeta `prueba_estudiante\` con **solo** el enunciado y una **copia** del `.pka`.
- Solo puede abrir la actividad (`pt_activity_open`) y configurar como un estudiante: `pt_cli`, `pt_host_ip_config` y `pt_host_command`.
- **Prohibido:** `pt_activity_check`, `pt_activity_status`, `pt_activity_tree`, `pt_activity_mark`, `pt_activity_save`, `pt_send_raw` y cualquier herramienta que lea el checklist o la red de respuesta, o que guarde archivos. `pt_activity_check` muestra los valores esperados de cada hoja.
- Debe listar todo lo que le pareció **ambiguo** en el enunciado.

Al terminar, la IA principal lee el porcentaje con `pt_activity_check`. La meta es **100 %**. Si no se llega, diagnostique con las hojas incorrectas (*Check Results*) antes de cambiar nada.

El texto de la petición está en la skill: `reference/prompt-estudiante.md`.

### Variante "desde cero"

El subagente parte de un lienzo vacío, construye toda la red y se audita contra el solucionario. Mide si el enunciado alcanza para reconstruir la red completa. **No** sustituye a la prueba con la red inicial.

> En la práctica 3.3, el primer 100 % se consiguió **sin querer** con esta variante: el `.pka` del docente tenía la red inicial vacía. Desde entonces se comprueba siempre que la red inicial tenga equipos.

## 3. Resultado de referencia: práctica 3.3 (Clínica Valle Sereno)

| Criterio | Resultado |
|---|---|
| Ítems tras reabrir | 42 (luego 38, sin las 4 hojas VTY Login que ya venían correctas) |
| Red inicial | 12 equipos |
| Porcentaje inicial | 9,5 % con 42 ítems; **0 %** con 38 |
| Prueba del estudiante | **42/42 = 100 %**, en unos 3 minutos y 20 llamadas a herramientas |
| Ambigüedades encontradas | El enunciado decía que el archivo de trabajo era `.pkt` en vez de `.pka`; faltaba avisar que el primer ping tras cambiar una VLAN puede fallar; no queda claro si hace falta `mls qos` global |

Las dos primeras ambigüedades se corrigieron en el enunciado y en las instrucciones.
