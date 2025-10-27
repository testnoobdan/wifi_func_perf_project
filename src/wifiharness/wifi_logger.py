import json, time, os
LOG_PATH = "reports/wifi_log.jsonl"

def log_event(action, status, extra=None):
    rec = {"ts": time.time(), "action": action, "status": status}
    if extra: rec.update(extra)
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f: f.write(json.dumps(rec)+"\n")
