.PHONY: up down restart logs db-shell dev

# เปิด MongoDB
up:
	docker compose up -d
	source venv/bin/activate
	cd order_service && python -m uvicorn app.main:app --reload

# ปิด MongoDB
down:
	docker compose down --remove-orphans

# restart MongoDB
restart:
	docker compose restart

# ดู logs MongoDB
logs:
	docker compose logs -f mongo

# เข้า MongoDB shell
db-shell:
	docker exec -it local-mongo mongosh

ps:
	docker-compose ps