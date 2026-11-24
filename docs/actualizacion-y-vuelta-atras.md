# Actualización del MCP y vuelta atrás

Esta guía explica cómo pasar a una versión nueva de `packet-tracer-mcp` guardando la anterior, y cómo volver a ella si algo falla. Así se pasó de la 0.9.0 a la 0.12.0 el 24 de noviembre de 2026, en Windows (PowerShell).

## 1. Respaldo

Guarde la versión instalada, la skill y la extensión que usa hoy:

```powershell
New-Item -ItemType Directory -Force "$HOME\pt-backup"
pip freeze --user > "$HOME\pt-backup\pip-antes.txt"
pip show packet-tracer-mcp > "$HOME\pt-backup\packet-tracer-mcp-anterior.txt"
Copy-Item -Recurse "$HOME\.claude\skills\packet-tracer" "$HOME\pt-backup\skill-packet-tracer-anterior"
Copy-Item "$HOME\Downloads\MCP-Control-Center.pts" "$HOME\pt-backup\MCP-Control-Center_anterior.pts"
```

Ajuste la última línea si su `.pts` está en otra carpeta.

## 2. Actualización

1. Instale la versión nueva desde PyPI con el extra `[ui]`:
   ```powershell
   pip install --user "packet-tracer-mcp[ui]==0.12.0"
   ```
   Es preferible usar PyPI a `pip install -e .` desde este repositorio: una instalación editable ata el MCP a la carpeta del repositorio, y esa carpeta cambia cuando usted edita la documentación.
2. Actualice la skill `packet-tracer` con la carpeta `skill/` de la misma versión:
   ```powershell
   Remove-Item -Recurse "$HOME\.claude\skills\packet-tracer"
   Copy-Item -Recurse "C:\ruta\al\repo\skill" "$HOME\.claude\skills\packet-tracer"
   ```
3. Descargue el `MCP-Control-Center.pts` de la misma release. En Packet Tracer, quite el módulo anterior en **Extensions → Scripting → Configure PT Script Modules** y agregue el nuevo. **Reinicie Packet Tracer.**
4. **Cierre la app de Claude por completo**: clic derecho en el icono de la bandeja del sistema → **Quit**. Cerrar solo la ventana no basta, porque los servidores MCP que ya estaban en marcha siguen ejecutando el código anterior.
5. Vuelva a abrir Claude y compruebe:
   - `/mcp` muestra el servidor `packet-tracer` con el número de herramientas de la versión nueva. La 0.12.0 tiene 111; la 0.9.0 tenía 61.
   - Debe haber **un solo** proceso del servidor:
     ```powershell
     Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*packet_tracer_mcp*' } | Select-Object ProcessId, CreationDate
     ```
     Su hora de inicio debe ser **posterior** a la instalación.

## 3. Vuelta atrás

```powershell
pip install --user packet-tracer-mcp==0.9.0
Remove-Item -Recurse "$HOME\.claude\skills\packet-tracer"
Copy-Item -Recurse "$HOME\pt-backup\skill-packet-tracer-anterior" "$HOME\.claude\skills\packet-tracer"
```

Después:

1. Cargue en Packet Tracer el `.pts` respaldado.
2. Reinicie Packet Tracer.
3. Cierre la app de Claude por completo y vuelva a abrirla.

No hace falta repetir `claude mcp add`: el registro (`python -m packet_tracer_mcp --stdio`) es el mismo en las dos versiones.
