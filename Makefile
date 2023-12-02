.PHONY: test

test:
	@pytest -v

test-coverage:
	@pytest -v --cov=src --cov-report=term-missing

lint:
	@ruff check .

format:
	@ruff format .
