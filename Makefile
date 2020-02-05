.PHONY: vsetup
vsetup:
	test -d venv || virtualenv-3.7 -p /usr/bin/python3.7 venv

.PHONY: test
test:
	pytest -sv tests/

.PHONY: clean
clean:
	find . -name '*.pyc' -delete -print
	find . -name '*.pyo' -delete -print
	find . -name '*~' -delete -print
	find . -name '__pycache__' -delete -print

.PHONY: distclean
distclean:
	git clean -fdX
