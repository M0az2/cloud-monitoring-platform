.PHONY: help up down logs restart status

help:
	@echo "Cloud-Native Monitoring Platform"
	@echo "=================================="
	@echo "make up      - Start all services"
	@echo "make down    - Stop all services"
	@echo "make logs    - View logs"
	@echo "make restart - Restart services"
	@echo "make status  - Check service status"
	@echo "make clean   - Remove data volumes"

up:
	@docker compose up -d
	@echo "Services started"

down:
	@docker compose down
	@echo "Services stopped"

logs:
	@docker compose logs -f

restart:
	@docker compose restart
	@echo "Services restarted"

status:
	@docker compose ps

clean:
	@docker compose down -v
	@echo "Services and data removed"

