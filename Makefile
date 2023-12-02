.PHONY: welcome test test-coverage lint format generate-requirements install build clean help
.DEFAULT_GOAL := help

welcome:
	@echo "   _____                       __                               "
	@echo "  / ___/__  ______  ___  _____/ /   ____  ____ _____ ____  _____"
	@echo "  \__ \/ / / / __ \/ _ \/ ___/ /   / __ \/ __ `/ __ `/ _ \/ ___/"
	@echo " ___/ / /_/ / /_/ /  __/ /  / /___/ /_/ / /_/ / /_/ /  __/ /    "
	@echo "/____/\__,_/ .___/\___/_/  /_____/\____/\__, /\__, /\___/_/     "
	@echo "          /_/                          /____//____/           \n"
	@echo " SuperLogger is a simple and powerful Python logger that provides flexibility and ease of use.\n"
	@echo " See https://github.com/Pelegrinetti/python-superlogger for more information.\n"

test:
	@echo "Running tests"
	@pytest -v

setup: install
	@echo "Setting up"
	@pre-commit install

test-coverage:
	@pytest -v --cov=src --cov-report=term-missing

lint:
	@echo "Running linter"
	@ruff check .

format:
	@echo "Running formatter"
	@ruff format .

generate-requirements:
	@echo "Generating requirements.txt"
	@echo "Add Poetry export plugin"
	@poetry self add poetry-plugin-export
	@poetry export --output requirements.txt

install:
	@echo "Installing dependencies"
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
	@echo "  welcome				Display the welcome message"
	@echo "  test					Run tests"
	@echo "  test-coverage			Run tests with coverage"
	@echo "  lint					Run linting checks"
	@echo "  format					Format code"
	@echo "  generate-requirements	Generate requirements.txt"
	@echo "  install				Install dependencies"
	@echo "  build					Build the package"
	@echo "  clean					Clean the package"
	@echo "  setup					Set up the project"
	@echo "  help					Show this help message"
