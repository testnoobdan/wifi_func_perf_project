
# Wi-Fi Automation Harness  

[![CI](https://github.com/testnoobdan/wifi_automation_harness/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/wifi_automation_harness/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](#)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lint: flake8](https://img.shields.io/badge/lint-flake8-blue)](#)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)


# Wi-Fi Automation Harness  

A modular Quality Engineering framework for validating Wi-Fi connectivity, interoperability, and throughput across macOS and Linux platforms.  
Designed following the **SEL-9 scalable engineering loop**: Spec → UML → Tests → Code → Automation → Observability.

---

## Overview
This harness is intended for **system-level QE validation**, not application UI testing.  
It automates Wi-Fi actions such as scanning, connecting, and measuring throughput, while collecting structured KPIs for reporting and trend visualization.

---

## Key Components
- **pytest suite** — Connects/disconnects to known SSIDs via `networksetup` (macOS) or `nmcli` (Linux)  
- **Log collection & KPI extraction** — RSSI, PER, throughput (Mbps), connection latency  
- **SEL-9 integration** — Makefile, CI pipeline, and coverage enforcement  
- **Tentpole QE compatibility** — Exports JSONL/CSV metrics for dashboard ingestion  
- **SQLite/JSON datastore** — Optional persistence for multi-run aggregation

---

## Quickstart

```bash
# Create virtual environment
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
./Scripts/ta

# View logs
cat reports/wifi_log.jsonl
