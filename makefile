PYTHON := python
TEST_FILE := ./samples/test.theo
APP := app

.PHONY: run
run:
	uv run $(PYTHON) -m $(APP) $(TEST_FILE)

.PHONY: test
test:
	uv run $(PYTHON) -m unittest -v

.PHONY: doc
doc:
	mdbook serve doc