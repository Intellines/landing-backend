.PHONY: format lint fmt start

format:
	uv run isort src/

lint:
	uv run ruff format src/

fmt: format lint

start: fmt
	uv run src/main.py
