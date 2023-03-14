lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
install:
	poetry install
	poetry run pip install pytest
coverage:
	pytest --cov=gendiff tests/