lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
install:
	poetry install
	poetry add  pytest-cov
	poetry add flake8
test-cov:
	pytest --cov=gendiff tests/