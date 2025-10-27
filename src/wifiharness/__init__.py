"""
Wi-Fi Automation Harness Package

Exposes key modules:
- wifi_controller: handles scanning, connecting, and disconnecting
- wifi_metrics: measures ping and throughput
- wifi_logger: handles structured JSON logging
"""

from src.wifiharness.wifi_logger import log_event
from src.wifiharness.wifi_metrics import WiFiMetrics
from src.wifiharness.wifi_controller import WiFiController

__all__ = ["WiFiController", "WiFiMetrics", "log_event"]
