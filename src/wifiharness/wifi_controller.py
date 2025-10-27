import subprocess, json, time
from .wifi_logger import log_event

class WiFiController:
    def scan(self):
        """Return list of SSIDs visible to system."""
        cmd = ["networksetup", "-listallhardwareports"]
        out = subprocess.check_output(cmd).decode()
        log_event("scan", "success")
        return out

    def connect(self, ssid, password):
        start = time.time()
        try:
            subprocess.run(["networksetup", "-setairportnetwork", "en0", ssid, password], check=True)
            latency = (time.time() - start) * 1000
            log_event("connect", "success", {"ssid": ssid, "latency_ms": latency})
            return latency
        except subprocess.CalledProcessError as e:
            log_event("connect", "failure", {"error": str(e)})
            raise

    def disconnect(self):
        subprocess.run(["networksetup", "-setairportpower", "en0", "off"])
        time.sleep(1)
        subprocess.run(["networksetup", "-setairportpower", "en0", "on"])
        log_event("disconnect", "success")
