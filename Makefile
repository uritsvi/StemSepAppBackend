ifneq (,$(wildcard .env))
    include .env
    export
endif

build_container:
	. venv/bin/activate && pip freeze > requirements.txt
	docker build -t stem-sep-app-backend:latest .

run_container:
	docker run -it -p 8000:8000 stem-sep-app-backend:latest