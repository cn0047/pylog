.PHONY: test
test:
	pytest -s -vvv tests/integration/log.py

.PHONY: coverage
coverage:
	coverage run --source=realtimelog -m pytest tests/integration/log.py
	coveralls
