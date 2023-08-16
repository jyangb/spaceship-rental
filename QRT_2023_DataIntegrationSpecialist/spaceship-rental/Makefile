dep:
	. ./setup.sh

run-local:
	python3 app.py

build:
	docker build -t spaceship-app .

run-docker:
	docker run -p 8080:8080 spaceship-app
