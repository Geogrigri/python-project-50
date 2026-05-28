install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check gendiff tests
