.PHONY: init install install-dev build publish

init:
	pip install -r requirements.txt

install:
	pip install .

install-dev:
	pip install -e .

build:
	python -m build

publish:
	twine upload -r testpypi dist/*
