health:
	@curl -s localhost:8080/healthcheck | jq

build:
	docker-compose build

run:
	docker-compose up

build-run:
	make build
	make run

release:
	$(if ${VERSION},,$(error ENV is not defined))
	docker build --platform linux/amd64 -t ehan1990/simple-flask:${VERSION} .
	docker push ehan1990/simple-flask:${VERSION}
