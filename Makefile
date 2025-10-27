lint:
	@echo "Running flake8 linting..."
	flake8 src tests

test:
	./Scripts/ta

coverage:
	mkdir -p reports/coverage-html
	PYTHONPATH="$(PWD)/src:$$PYTHONPATH" python -m pytest --cov=src --cov-report=html:reports/coverage-html

all: lint test coverage