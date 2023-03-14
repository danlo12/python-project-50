lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
install:
	poetry install
coverage:
	pytest --cov=gendiff tests/