test:
	./Scripts/ta
coverage:
	pytest --cov=src --cov-report=html
all: test coverage
