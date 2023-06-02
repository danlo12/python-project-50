lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
install:
test-cov:
	poetry run pytest --cov=gendiff --cov-report xml