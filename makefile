PYTHON := python
TEST_FILE := ./samples/test.theo
APP := app

.PHONY: run
run:
	uv run $(PYTHON) -m $(APP) $(TEST_FILE)

.PHONY: test
test:
	uv run coverage run
	uv run coverage html

.PHONY: serve_coverage
serve_coverage:
	uv run python -m http.server -d htmlcov 9000

.PHONY: doc
doc:
	mdbook serve doc

.PHONY: java_serve_coverage
java_serve_coverage:
	uv run python -m http.server -d java/app/build/reports 9000
