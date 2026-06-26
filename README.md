
> # Cloud-Native Monitoring Platform
### Components
 Pometheus (Port 9090)
- Prometheus (Port 9090) time-series database
  - Metrics collection and time-series database
  - Scrape interval: 15 seconds
  - Retention: 15 days
  Grafana (Port 3000)
- Grafana (Port 3000)ashboard creation
- Visualization and dashboard creation
  - Default credentials: admin/admin
  - Data source: Prometheus
  Alertmanager (Port 9093)
- Alertmanager (Port 9093)ment
  - Alert routing and management
  - Webhook integration support
  Node Exporter (Port 9100)
- Node Exporter (Port 9100)ection
  - System-level metrics collectiontoring
  - CPU, Memory, Disk, Network monitoring
## Quick Start

### Prerequisites
> - Docker
- Docker Compose
- Linux/Unix environment

### Running

bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
> ### Access Points

> | Service | URL | Credentials |
|---------|-----|-------------|
| Grafana | http://localhost:3000 | admin/admin |
| Prometheus | http://localhost:9090 | N/A |
| Alertmanager | http://localhost:9093 | N/A |
| Node Exporter | http://localhost:9100 | N/A |

## Project Structure
> ├── prometheus/

│   ├── prometheus.yml       # Prometheus config

│   └── data/                # Time-series database

├── grafana/

│   └── data/                # Grafana database

├── alertmanager/

│   └── alertmanager.yml     # Alertmanager config

├── docker-compose.yml       # Container orchestration

└── README.md               # This file
## Key Metrics
> ### Available from Prometheus

- up - Service availability (0 or 1)
- node_cpu_seconds_total - CPU time spent
- node_memory_MemAvailable_bytes - Available memory
- node_filesystem_avail_bytes - Disk space available
- node_network_receive_bytes_total - Network ingress
## Configuration

### Prometheus Targets

Edit prometheus/prometheus.yml to add new targets:

yaml
scrape_configs:
  - job_name: 'my-service'
    static_configs:
      - targets: ['localhost:9090']
> ### Alerting Rules

Configure alerts in alertmanager/alertmanager.yml. Currently set to send webhooks to http://localhost:5001/.

## Design Decisions

1. Docker Compose - Simplicity and
