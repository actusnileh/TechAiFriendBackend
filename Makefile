DC = docker compose
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storages.yaml
ENV_FILE = --env-file .env

.PHONY: build
build:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} ${ENV_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: logs
logs:
	${DC} -f ${STORAGE_FILE} -f ${APP_FILE} ${ENV_FILE}  logs -f