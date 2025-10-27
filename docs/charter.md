
---

## 📜 2. `docs/charter.md`

```markdown
# Project Charter v1.0 — Wi-Fi Automation Harness

## Context
This project provides a lightweight, modular automation framework for testing Wi-Fi connectivity, performance, and reliability on macOS and Linux platforms.

## Problem Statement
Manual testing of Wi-Fi performance is error-prone and time-consuming.  
We need a deterministic, scriptable system that can connect to networks, measure performance, and log results for both local and CI validation.

## Objectives (Measurable)
- **O1:** Automate Wi-Fi connection & verification across environments
- **O2:** Ensure consistent throughput measurement (±5 % variance)
- **O3:** Collect structured logs suitable for Tentpole QE ingestion
- **O4:** Maintain ≥ 85 % test coverage enforced via CI

## Scope
**In Scope**
- SSID scanning, connection, disconnection
- Throughput & latency measurement
- Logging, JSON export, and coverage gate

**Out of Scope**
- Advanced 802.11ax PHY diagnostics
- Hardware-specific chipset debugging

## Success Criteria
| Metric | Target | Method |
|---------|---------|--------|
| P95 connection latency | ≤ 3 s | pytest |
| Test coverage | ≥ 85 % | GitHub Actions |
| Confidence level | High | Tentpole QE |
| Avg throughput | ≥ 50 Mbps | `curl`/`iperf3` |

## Risks / Assumptions
- Wi-Fi hardware must support system CLI access (`networksetup`/`nmcli`)
- CI runs are macOS or Linux-based
- Network environment may introduce external noise (non-deterministic results)
