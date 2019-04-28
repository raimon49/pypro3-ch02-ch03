DEV_DEPENDS='requirements'

.DEFAULT_GOAL:= help

# help	setup	Install devendencies via PyPI
.PHONY: setup
	pip install -r $(DEV_DEPENDS).txt

# help	local-install	Install app via pip install -e command
.PHONY: local-install
local-install:
	pip install -e .

# help	local-uninstall	Uninstall editable package
.PHONY: local-uninstall
local-uninstall:
	pip uninstall -y raimon49.norilog

# help	update-depends	Update requirements file
.PHONY: update-depends
update-depends:
	pip freeze > $(DEV_DEPENDS).txt

# help	build	Build Python package
.PHONY: build
build: clean
	python setup.py bdist_wheel

# help	check	Check package metadata
.PHONY: check
check:
	twine check dist/*.whl

# help	deploy	Upload package to Test PyPI server
.PHONY: deploy
deploy: build check
	twine upload -r pypitest dist/*

# help	clean	 Clean build files
.PHONY: clean
clean:
	python setup.py clean
	rm -rf dist

# help	help	 Show task list
.PHONY: help
help:
	@sed -n 's/# help//p' < Makefile
