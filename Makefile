lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest
install:
	poetry install
	poetry run pip install pytest
	poetry add pytest
coverage:
	pytest --cov=gendiff tests/