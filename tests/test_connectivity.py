
import pytest
from src.wifiharness.wifi_controller import WiFiController
from src.wifiharness.wifi_metrics import WiFiMetrics

@pytest.fixture(scope="module")
def wifi():
    return WiFiController()

def test_scan(wifi):
    out = wifi.scan()
    assert "Hardware Port" in out

def test_connectivity_cycle(wifi):
    latency = wifi.connect("MyHomeWiFi", "password123")
    assert latency < 3000
    metrics = WiFiMetrics()
    ping_result = metrics.ping()
    assert "0.0% packet loss" in ping_result
    wifi.disconnect()
