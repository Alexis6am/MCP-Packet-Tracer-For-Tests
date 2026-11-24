"""Importa un .pkt como red inicial del Activity Wizard (solo Windows).

Usa el driver de UI Automation que trae packet-tracer-mcp 0.12 (instalado con el
extra [ui]). Hace lo mismo que una persona: responde "Use as the Answer Network?"
si aparece, abre la página Initial Network, pulsa "Import File to Initial Network",
escribe la ruta en el diálogo y vuelve a la página Answer Network.

Uso (con el Activity Wizard ya abierto o a punto de preguntar):
    python importar_red_inicial.py "C:\\ruta\\Practica_X_Inicial.pkt"

Salida: una línea JSON {"ok": true|false, ...}. Si ok es false, haga el paso a mano.

Aviso: usa funciones internas del driver (no son API pública del MCP). Se verificó
con packet-tracer-mcp 0.12.0 y Packet Tracer 9.0.0 en Windows 11; con otra versión
puede dejar de funcionar.
"""
from __future__ import annotations

import json
import os
import sys
import time


def main() -> int:
    if len(sys.argv) != 2:
        print(json.dumps({"ok": False, "error": "Uso: importar_red_inicial.py <ruta del .pkt inicial>"}))
        return 2
    path = os.path.abspath(sys.argv[1])
    if not os.path.isfile(path):
        print(json.dumps({"ok": False, "error": f"No existe: {path}"}))
        return 2
    if os.name != "nt":
        print(json.dumps({"ok": False, "error": "Solo Windows: en macOS importe la red inicial a mano."}))
        return 2
    try:
        from packet_tracer_mcp.infrastructure.ui import win32
        from packet_tracer_mcp.infrastructure.ui.wizard import (
            WizardDriver, YES_NAMES, open_modals,
        )
    except ImportError as exc:
        print(json.dumps({"ok": False, "error": f"Falta packet-tracer-mcp[ui] 0.12: {exc}"}))
        return 2

    pids = win32.pt_pids()
    if len(pids) != 1:
        print(json.dumps({"ok": False, "error": f"Debe haber un solo Packet Tracer abierto; hay {len(pids)}."}))
        return 1
    pid = pids[0]
    d = WizardDriver(lambda _src, _t: str(pid))
    steps = []
    try:
        # 1. Al abrir el Wizard sobre un .pkt, PT pregunta si usar la red como respuesta.
        for _ in range(40):
            dlg = d._titled(pid, "Use as the Answer Network?")
            if dlg:
                d._press(dlg, YES_NAMES)
                steps.append("Use as the Answer Network? -> Yes")
                time.sleep(1.0)
                break
            if win32.find_window(pid, "Activity Wizard"):
                break
            time.sleep(0.25)
        # La ventana del Wizard tarda unos segundos en aparecer después del "Yes".
        for _ in range(60):
            if win32.find_window(pid, "Activity Wizard"):
                break
            time.sleep(0.25)
        time.sleep(1.0)
        hwnd = d._window(pid)
        # 2. Página Initial Network y botón Import File to Initial Network.
        d._page(hwnd, "m_initNetworkBtn")
        d._click(hwnd, d._find(hwnd, "m_importInitNetBtn"))
        dlg = d._wait_dialog(pid, "Import File")
        if not win32.fill_file_dialog(dlg, path):
            win32.cancel_dialog(dlg)
            raise RuntimeError("El diálogo Import File no tiene campo de nombre.")
        steps.append(f"Import File -> {path}")
        time.sleep(2.0)
        left = open_modals()
        if left:
            raise RuntimeError(f"Quedó un diálogo abierto: {left}")
        # 3. Volver a Answer Network.
        d._page(hwnd, "m_answerNetworkBtn")
        steps.append("Answer Network")
    except Exception as exc:  # noqa: BLE001 - cualquier fallo se informa y se hace a mano
        print(json.dumps({"ok": False, "error": str(exc), "steps": steps}, ensure_ascii=False))
        return 1
    print(json.dumps({"ok": True, "steps": steps}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
