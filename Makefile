lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
install:
	poetry install
	poetry install pytest-cov
	poetry install coverage
	poetry add flake8
test-cov:
	pytest --cov=gendiff tests/