all:
	docker-compose up --build --force-recreate -d

stop: 
	docker-compose down
stop-reset:
	docker-compose down -v