# Wi-Fi Automation Harness Spec v0.1

## Functional Requirements
FR-01: Scan available SSIDs.
FR-02: Connect to a specified SSID with stored credentials.
FR-03: Verify IP acquisition & internet reachability.
FR-04: Measure throughput using `iperf3` or curl download.
FR-05: Disconnect and clean up.

## Non-Functional Requirements
NFR-01: Pass rate ≥ 95 % across 10 runs.
NFR-02: Mean connection latency ≤ 3 s.
NFR-03: Logs and metrics exported in JSON & CSV.

## Observability
Metrics: `connect_time_ms`, `rssi_dbm`, `throughput_mbps`, `packet_loss_%`
Logs: `{timestamp, ssid, action, result, error?}`
