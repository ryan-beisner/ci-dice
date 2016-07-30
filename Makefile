#!/usr/bin/make
PYTHON := /usr/bin/env python3

lint:
	@tox -e pep8

test:
	@echo Starting unit tests...
	@tox -e py27

clean:
	@snapcraft clean

build:
	@snapcraft snap
