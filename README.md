# Cloud Monitoring Platform

A production-ready monitoring stack built with Docker Compose, featuring real-time metrics, alerting, and dashboards — all configured as code.

## Stack

| Service | Role | Port |
|---------|------|------|
| Prometheus | Metrics collection & alerting | 9090 |
| Grafana | Dashboards & visualization | 3000 |
| Alertmanager | Alert routing & notifications | 9093 |
| Node Exporter | Host system metrics | 9100 |
| cAdvisor | Container metrics | 8080 |
| Webhook Receiver | Alert webhook handler | 5001 |

## Architecture

```
Node Exporter ──┐
cAdvisor        ├──► Prometheus ──► Alertmanager ──► Webhook Receiver
Prometheus self ┘         │
                          ▼
                       Grafana
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Run

```bash
# Clone the repo
git clone https://github.com/M0az2/cloud-monitoring-platform.git
cd cloud-monitoring-platform

# Start the stack
docker compose up -d

# Check all services are running
docker compose ps
```

### Access

| URL | Credentials |
|-----|-------------|
| http://localhost:3000 | admin / admin |
| http://localhost:9090 | — |
| http://localhost:9093 | — |
| http://localhost:5001/health | — |

## Features

### Grafana Provisioning
Datasource and dashboards are automatically configured on startup — no manual setup required.

Dashboard includes:
- CPU Usage %
- Memory Usage %
- Disk Usage %
- Available Memory
- Network RX/TX
- Service Status (all targets)

### Alert Rules
9 alerting rules across 4 groups:

| Alert | Condition | Severity |
|-------|-----------|----------|
| InstanceDown | target unreachable > 1m | critical |
| HighCPUUsage | CPU > 80% for 5m | warning |
| CriticalCPUUsage | CPU > 95% for 2m | critical |
| HighMemoryUsage | Memory > 80% for 5m | warning |
| CriticalMemoryUsage | Memory > 95% for 2m | critical |
| DiskSpaceWarning | Disk > 75% for 5m | warning |
| DiskSpaceCritical | Disk > 90% for 2m | critical |
| HighNetworkReceive | RX > 100MB/s for 5m | warning |

### Webhook Receiver
A lightweight Flask service that receives alerts from Alertmanager.

```bash
# View received alerts
curl http://localhost:5001/alerts

# Health check
curl http://localhost:5001/health
```

## CI/CD

GitHub Actions runs on every push and PR to `main`:

- ✅ Validate `prometheus.yml`
- ✅ Validate `rules.yml`
- ✅ Validate `alertmanager.yml`
- ✅ Validate `docker-compose.yml`
- ✅ Build webhook-receiver Docker image

## Project Structure

```
cloud-monitoring-platform/
├── prometheus/
│   ├── prometheus.yml        # Scrape configs & alertmanager connection
│   └── rules.yml             # Alerting rules
├── grafana/
│   └── provisioning/
│       ├── datasources/      # Auto-configured Prometheus datasource
│       └── dashboards/       # Auto-loaded Node Exporter dashboard
├── alertmanager/
│   └── alertmanager.yml      # Alert routing & webhook config
├── webhook-receiver/
│   ├── app.py                # Flask webhook handler
│   ├── Dockerfile
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml            # Config validation pipeline
├── docker-compose.yml
└── .env.example
```

## Useful Commands

```bash
# Start
docker compose up -d

# Stop
docker compose down

# View logs
docker compose logs -f

# Restart a service
docker compose restart grafana

# Check status
docker compose ps
