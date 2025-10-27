import subprocess, json, statistics
from .wifi_logger import log_event

class WiFiMetrics:
    def ping(self, host="8.8.8.8", count=5):
        res = subprocess.run(["ping", "-c", str(count), host], capture_output=True, text=True)
        log_event("ping", "success" if res.returncode==0 else "failure")
        return res.stdout

    def throughput(self, host="speedtest.tele2.net", size_mb=10):
        cmd = ["curl", "-o", "/dev/null", f"http://{host}/{size_mb}MB.zip", "-s", "-w", "%{speed_download}"]
        out = subprocess.check_output(cmd).decode().strip()
        mbps = round(float(out)/1e6*8,2)
        log_event("throughput", "success", {"mbps": mbps})
        return mbps
