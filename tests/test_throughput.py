import pytest
from src.wifiharness import WiFiController, WiFiMetrics

@pytest.fixture(scope="module")
def wifi_controller():
    """Fixture for WiFi controller lifecycle."""
    controller = WiFiController()
    yield controller
    controller.disconnect()  # cleanup at end of module

@pytest.fixture(scope="module")
def wifi_metrics():
    """Fixture for WiFi metrics utility."""
    return WiFiMetrics()
