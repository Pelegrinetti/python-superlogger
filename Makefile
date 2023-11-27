.PHONY: test

test:
	@pytest -v

lint:
	@ruff check .

format:
	@ruff format .
