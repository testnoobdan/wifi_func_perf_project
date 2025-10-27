import subprocess
import pytest

# Import your public API (clean, no "src." in imports)
from src.wifiharness.wifi_controller import WiFiController
from src.wifiharness.wifi_metrics import WiFiMetrics  # noqa: F401


@pytest.fixture
def wifi():
    """Basic controller fixture used by tests."""
    # keep "en0" default; it's harmless under the mock
    return WiFiController(interface="en0")


@pytest.fixture(autouse=True)
def prevent_real_network(request, monkeypatch):
    """
    Autouse fixture: mock subprocess.run so unit tests never touch the OS.
    Returns realistic stdout for common Wi-Fi commands used by the harness.
    Opt-out by marking a test with @pytest.mark.real_network.
    """
    if request.node.get_closest_marker("real_network"):
        # Allow specific tests to exercise the real system
        return

    class FakeCompleted:
        def __init__(self, returncode=0, stdout=b"", stderr=b"", args=None):
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr
            self.args = args

    def _as_bytes_or_str(s, want_text):
        # If the caller asked for text=True / universal_newlines=True, return str
        # Otherwise return bytes, like real subprocess.run would.
        if want_text:
            return s
        return s.encode("utf-8")

    def fake_run(*args, **kwargs):
        cmd = args[0] if args else kwargs.get("args")
        want_text = bool(kwargs.get("text") or kwargs.get("universal_newlines"))

        # Normalize command to a list of strings
        if isinstance(cmd, (tuple, list)):
            cmd_list = list(map(str, cmd))
        elif isinstance(cmd, str):
            cmd_list = [cmd]
        else:
            cmd_list = []

        stdout = ""
        stderr = ""
        rc = 0

        # 1) macOS: list hardware ports
        if cmd_list[:2] == ["networksetup", "-listallhardwareports"]:
            stdout = (
                "Hardware Port: Wi-Fi\n"
                "Device: en0\n"
                "Ethernet Address: aa:bb:cc:dd:ee:ff\n\n"
                "Hardware Port: Thunderbolt Ethernet\n"
                "Device: en1\n"
                "Ethernet Address: 11:22:33:44:55:66\n"
            )

        # 2) macOS: connect to SSID
        elif cmd_list[:2] == ["networksetup", "-setairportnetwork"]:
            stdout = ""
            rc = 0

        # 3) airport scan
        elif cmd_list and ("airport" in cmd_list[0]) and ("-s" in cmd_list):
            stdout = (
                "                           SSID BSSID             RSSI CHANNEL HT CC SECURITY\n"
                "                      MyHomeWiFi aa:bb:cc:dd:ee:ff -40  149     Y  US WPA2(PSK/AES)\n"
                "                    CoffeeShopWiFi 11:22:33:44:55:66 -67   11     N  US WEP\n"
            )

        # 4) ping (simulate success with 0.0% loss)
        elif cmd_list and ("ping" in cmd_list[0] or cmd_list[0].endswith("/ping")):
            target = "8.8.8.8"
            # macOS-style summary with 0.0% packet loss
            stdout = (
                f"PING {target} ({target}): 56 data bytes\n"
                f"64 bytes from {target}: icmp_seq=0 ttl=115 time=14.123 ms\n\n"
                f"--- {target} ping statistics ---\n"
                "1 packets transmitted, 1 packets received, 0.0% packet loss\n"
                "round-trip min/avg/max/stddev = 14.123/14.123/14.123/0.000 ms\n"
            )
            rc = 0

        # 5) default
        else:
            stdout = ""

        def _as_bytes_or_str(s, want_text_flag):
            return s if want_text_flag else s.encode("utf-8")

        return FakeCompleted(
            returncode=rc,
            stdout=_as_bytes_or_str(stdout, want_text),
            stderr=_as_bytes_or_str(stderr, want_text),
            args=cmd,
        )

    monkeypatch.setattr(subprocess, "run", fake_run)


def pytest_configure(config):
    # Register our custom marker to avoid warnings
    config.addinivalue_line(
        "markers",
        "real_network: run this test against the real OS (disables subprocess mock)",
    )
