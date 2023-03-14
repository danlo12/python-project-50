lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
install:
	poetry install
coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/