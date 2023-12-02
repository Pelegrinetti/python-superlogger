.PHONY: welcome test test-coverage lint format generate-requirements install build clean help
.DEFAULT_GOAL := help

welcome:
	@echo "   _____                       __                               "
	@echo "  / ___/__  ______  ___  _____/ /   ____  ____ _____ ____  _____"
	@echo "  \__ \/ / / / __ \/ _ \/ ___/ /   / __ \/ __ `/ __ `/ _ \/ ___/"
	@echo " ___/ / /_/ / /_/ /  __/ /  / /___/ /_/ / /_/ / /_/ /  __/ /    "
	@echo "/____/\__,_/ .___/\___/_/  /_____/\____/\__, /\__, /\___/_/     "
	@echo "          /_/                          /____/                   "

test:
	@pytest -v

test-coverage:
	@pytest -v --cov=src --cov-report=term-missing

lint:
	@ruff check .

format:
	@ruff format .

generate-requirements:
	@poetry export --output requirements.txt

install:
	@poetry install

build: install clean generate-requirements
	@echo "Building package"
	@poetry build
	@echo "Done"

clean:
	@echo "Cleaning package"
	@rm -rf requirements.txt
	@rm -rf dist

help: welcome
	@echo "Available targets:"
	@echo "  welcome             Display the welcome message"
	@echo "  test                Run tests"
	@echo "  test-coverage       Run tests with coverage"
	@echo "  lint                Run linting checks"
	@echo "  format              Format code"
	@echo "  generate-requirements Generate requirements.txt"
	@echo "  install             Install dependencies"
	@echo "  build               Build the package"
	@echo "  clean               Clean the package"
	@echo "  help                Show this help message"
