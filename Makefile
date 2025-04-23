.PHONY: sort lint fmt start

sort:
	uv run isort src/

lint:
	uv run ruff format src/

fmt: sort lint

start:
	uv run src/main.py
