import subprocess
from typing import Tuple


class WiFiMetrics:
    """Lightweight metrics helpers for connectivity tests."""

    def ping(self, target: str = "8.8.8.8", count: int = 1) -> str:
        """
        Run a small ping and return the raw output (tests assert on packet loss text).
        """
        result = subprocess.run(
            ["ping", "-c", str(count), target],
            check=False,
            capture_output=True,
            text=True,
        )
        return result.stdout or ""

    @staticmethod
    def parse_packet_loss(ping_output: str) -> Tuple[int, int, float]:
        """
        Parse ping summary like:
        '1 packets transmitted, 1 packets received, 0.0% packet loss'
        Returns (tx, rx, loss_percent).
        """
        tx = rx = 0
        loss = 0.0
        for line in ping_output.splitlines():
            line = line.strip()
            if "packets transmitted" in line and "packet loss" in line:
                # Very lenient parse to handle macOS/Linux formats
                parts = line.replace(",", "").split()
                # e.g. ["1","packets","transmitted","1","packets","received","0.0%","packet","loss"]
                try:
                    tx = int(parts[0])
                    rx = int(parts[3])
                    loss_str = parts[6].rstrip("%")
                    loss = float(loss_str)
                except (IndexError, ValueError):
                    pass
                break
        return tx, rx, loss
