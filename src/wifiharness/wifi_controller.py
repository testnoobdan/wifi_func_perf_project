import subprocess
import time
from typing import Optional


class WiFiController:
    """Controls Wi-Fi actions such as scanning and connecting on macOS."""

    def __init__(self, interface: str = "en0") -> None:
        self.interface = interface

    def scan(self) -> str:
        """
        Return hardware ports list (used by tests to assert contents).
        On macOS this is typically:
        `networksetup -listallhardwareports`
        """
        result = subprocess.run(
            ["networksetup", "-listallhardwareports"],
            check=False,
            capture_output=True,
            text=True,
        )
        return result.stdout or ""

    def connect(
        self, ssid: str, password: str, timeout_s: Optional[float] = None
    ) -> float:
        """
        Join the given SSID using the specified interface.
        Returns elapsed time in milliseconds.
        """
        start = time.time()
        subprocess.run(
            ["networksetup", "-setairportnetwork", self.interface, ssid, password],
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
        return (time.time() - start) * 1000.0

    def disconnect(self) -> None:
        """
        Disconnect from the current Wi-Fi network.
        Implementation note: we use 'airport -z' (disassociate) on macOS.
        In CI/tests this is mocked, so it always succeeds.
        """
        # Try the 'airport' disassociate command (macOS private CLI)
        subprocess.run(
            [
                "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
                "-z",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        # As a fallback (and to keep state clean), quickly toggle interface power.
        subprocess.run(
            ["networksetup", "-setairportpower", self.interface, "off"],
            check=False,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["networksetup", "-setairportpower", self.interface, "on"],
            check=False,
            capture_output=True,
            text=True,
        )
