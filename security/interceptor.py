#!/usr/bin/env python3
"""
Skeleton intercettore globale ZDOS-e660.
Intercetta richieste, logga attacchi, parla con K.I.R.A.
"""
import json
import time
from pathlib import Path

LOG_PATH = Path("/var/log/zdos-attacks.log")

def log_attack(data: dict):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {"ts": time.time(), "event": "attack", **data}
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[CAPTURE] {entry}")

def notify_kira(payload: dict):
    # Stub: in produzione socket/IPC verso processo KIRA
    print(f"[KIRA] notifica: {payload}")
    return {"action": "log_and_monitor"}

def handle_incoming(request: dict):
    print(f"[INTERCEPT] {request}")
    if request.get("suspicious"):
        log_attack(request)
        decision = notify_kira(request)
        return decision
    return {"action": "allow"}

if __name__ == "__main__":
    # Demo
    handle_incoming({"src": "192.168.1.100", "suspicious": True, "payload": "test-attack"})
