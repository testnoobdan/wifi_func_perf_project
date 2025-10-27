test:
	./Scripts/ta

coverage:
	mkdir -p reports/coverage-html
	pytest --cov=src --cov-report=html:reports/coverage-html

all: test coverage