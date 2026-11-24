# Instrucciones HTML de la actividad

Las instrucciones son lo que el estudiante ve en la ventana de la actividad, en Packet Tracer. Este proyecto usa **una sola página HTML** por actividad.

## Por qué una sola página

- `pt_activity_set_instructions` escribe **solo la primera página** de instrucciones.
- Con una página no hay que volver a la página 1 antes de guardar, ni pegar varias páginas a mano.
- En la práctica 3.3 se unieron 4 páginas en una (unos 9 000 caracteres). Packet Tracer la guardó **idéntica**, con sus estilos.

## Cómo escribirla

- Un documento HTML **completo**, con los estilos dentro de `<style>` en el `<head>`. Vea la plantilla [`templates/instrucciones_unificada.html`](../templates/instrucciones_unificada.html).
- Separe las partes con `<hr>` y títulos `<h2>`. No ponga pies del tipo "Página X de Y".
- Use tablas para el direccionamiento, las VLANs y los pings esperados.
- Escriba **todo lo que se califica**: hostnames, nombres de VLAN, contraseñas, puertos, IPs. El estudiante no tiene otra fuente dentro de Packet Tracer.
- Agregue los consejos que eviten falsos fallos. Por ejemplo: "si el primer ping falla justo después de cambiar un puerto de VLAN, espere unos segundos y repítalo".
- No incluya comandos de la solución.

## Cómo pegarla

**Con la IA (método oficial, Windows):** con el Wizard abierto, la IA llama a `pt_activity_set_instructions(html)`. La respuesta debe decir `html_preserved: true` e `identical: true`. Por dentro usa *Import Page* con un archivo temporal, que es la única vía que conserva el HTML.

**A mano:** Wizard → **Instructions → Plain Editor** → pegue el HTML completo. El *Rich Editor* deja un resultado plano, sin estilos.

**macOS:** el HTML solo se conserva si el servidor tiene `PT_UI_ALLOW_FOREGROUND=1`. Sin esa variable se guarda como texto plano. Vea [Instalación en macOS](instalacion-macos.md).

## Comprobación

Tras guardar y reabrir el `.pka`:

```javascript
var s = String(ipc.appWindow().getActiveFile().getInstructionSource(0));
reportResult(JSON.stringify({largo: s.length, estilos: s.indexOf("<style") >= 0}));
```

`pt_activity_status` también muestra las instrucciones como texto.
