# Verificaciones por API

Envíe cada una con `pt_send_raw(código, wait_result=True)`, en una sola línea y dentro de `try { … } catch (e) { reportResult("ERR " + e); }`.

## Estado del Wizard y de las redes

```javascript
var aw = ipc.appWindow(); var f = aw.getActiveFile();
reportResult(JSON.stringify({
  wizard: !!aw.isActivityWizardOpen(), actividad: f.isActivityFile(),
  archivo: String(f.getSavedFilename()),
  items: f.getAssessmentItemsCount(), arbol: f.getComparatorTree().getCheckLeafCount(),
  porcentaje: f.getPercentageComplete(),
  inicial: f.getInitNetworkFile().getMainNetwork().getDeviceCount(),
  respuesta: f.getAnsNetworkFile().getMainNetwork().getDeviceCount(),
  usuario: f.getUserNetworkFile().getMainNetwork().getDeviceCount()}));
```

- Con un `.pka` abierto, `ipc.network()` y `pt_query_topology` devuelven **0 equipos**: use las tres redes de arriba.
- Dentro del Wizard, `getSavedFilename()` puede salir vacío.

## Comprobar que la red inicial es la correcta

Compare un valor que difiera entre la red inicial y la de respuesta:

```javascript
var n = f.getInitNetworkFile().getMainNetwork();
reportResult(String(n.getDevice("PC-AUX-01").getPort("FastEthernet0").getIpAddress()));
```

## Instrucciones guardadas

```javascript
var s = String(f.getInstructionSource(0));
reportResult(JSON.stringify({largo: s.length, estilos: s.indexOf("<style") >= 0}));
```

## Abrir el Wizard sobre el archivo abierto

```javascript
ipc.appWindow().fileActivityWizard();
```

- Envíelo con **`wait_result=False`**.
- Sobre un `.pkt`, Packet Tracer pregunta "Use as the Answer Network?" y la llamada no vuelve hasta que alguien responde; `scripts/importar_red_inicial.py` contesta *Yes*.
- Sobre un `.pka`, el Wizard se abre directamente (verificado).

## No usar

- `getCheckOnlyTree()` para listar ítems: devuelve cientos de hojas que no son ítems.
- `pt_activity_check` en la prueba del estudiante: muestra las respuestas.
