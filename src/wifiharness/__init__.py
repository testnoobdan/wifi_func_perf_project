"""
Wi-Fi Automation Harness Package

Exposes key modules:
- wifi_controller: handles scanning, connecting, and disconnecting
- wifi_metrics: measures ping and throughput
- wifi_logger: handles structured JSON logging
"""

from .wifi_controller import WiFiController
from .wifi_metrics import WiFiMetrics
from .wifi_logger import log_event
