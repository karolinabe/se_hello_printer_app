.PHONY: test

deps:
	pip install -r requirement.txt ; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. py.test
	PYTHONPATH=. py.test  --verbose -s

run:
	python main.py

docker_build:
	docker build -t hello-world-printer .
