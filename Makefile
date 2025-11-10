.PHONY: help install test lint format clean docs

help:
	@echo "SynarkOS Development Commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make docs       - Build documentation"

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v --cov=synarkos --cov-report=term-missing

lint:
	ruff check synarkos tests
	mypy synarkos

format:
	black synarkos tests examples
	ruff check --fix synarkos tests examples

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete

docs:
	cd docs && make html
