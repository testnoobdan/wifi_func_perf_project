import json
from datetime import datetime
from typing import Any, Dict


def log_event(event: str, **fields: Any) -> str:
    """
    Produce a structured JSON log line for test artifacts.
    Returns the JSON string (does not write to disk/STDOUT).
    """
    payload: Dict[str, Any] = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "event": event,
        **fields,
    }
    return json.dumps(payload, separators=(",", ":"), sort_keys=True)
