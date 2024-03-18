install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest

lint:
	poetry run flake8