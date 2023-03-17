lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
install:
	poetry install
	poetry add flake8
	poetry add  pytest-cov
test-cov:
	pytest --cov=gendiff tests/