.PHONY: docker
docker:
	docker build -t fast-api-hello-world:latest .
	docker tag fast-api-hello-world:latest mikaelsouza/fast-api
	docker push mikaelsouza/fast-api

.PHONY: requirements
requirements:
	python -m pip install -r requirements.txt

.PHONY: dev-requirements
dev-requirements:
	python -m pip install -r requirements.dev.txt