all: install-requirements run

clear-pyc:
	find . -name "*.pyc" -exec rm -f {} \;

run:
	python -m grafana_noti.api

install-requirements:
	pip install -r requirements.txt

docker-build: clear-pyc
	docker build -t grafana-custom-noti:0.1 -f docker/dockerfile .