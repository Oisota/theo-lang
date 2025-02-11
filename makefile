PYTHON := python3
TEST_FILE := ./samples/test.theo
APP := app

.PHONY: run
run:
	$(PYTHON) -m $(APP) $(TEST_FILE)

.PHONY: test
test:
	$(PYTHON) -m unittest

.PHONY: doc
doc:
	mdbook serve doc