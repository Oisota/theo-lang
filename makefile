PYTHON := python3
TEST_FILE := ./samples/test.theo
APP := app

.PHONY: test
test:
	$(PYTHON) -m $(APP) $(TEST_FILE)