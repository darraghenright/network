SHELL := /bin/bash

.PHONY: help up down

help:
	@echo "Welcome! use \`make up\` and \`make down\` to start and stop the projects."

up:
	docker compose -f ./api/docker-compose.yaml up -d
	docker compose -f ./service/docker-compose.yaml up -d
	@echo "Visit http://localhost:5000/"

down:
	docker compose -f ./api/docker-compose.yaml stop
	docker compose -f ./service/docker-compose.yaml stop
	docker compose -f ./api/docker-compose.yaml down
	docker compose -f ./service/docker-compose.yaml down