# Refer to davidhalter/jedi-vim.
BUILD_VIRTUAL_ENV:=build/venv

$(dir $(BUILD_VIRTUAL_ENV)):
	mkdir -p $@

$(BUILD_VIRTUAL_ENV): | $(dir $(BUILD_VIRTUAL_ENV))
	python3 -m venv $@
	# $|/bin/python -m pip upgrade

$(BUILD_VIRTUAL_ENV)/bin/isort: | $(BUILD_VIRTUAL_ENV)
	$|/bin/python -m pip install -q isort==4.3.21

$(BUILD_VIRTUAL_ENV)/bin/yapf: | $(BUILD_VIRTUAL_ENV)
	$|/bin/python -m pip install -q yapf==0.30.0

isort: $(BUILD_VIRTUAL_ENV)/bin/isort
	$(BUILD_VIRTUAL_ENV)/bin/isort --help

yapf: $(BUILD_VIRTUAL_ENV)/bin/yapf
	$(BUILD_VIRTUAL_ENV)/bin/yapf --help
	mkdir -p config
	$(BUILD_VIRTUAL_ENV)/bin/yapf --style="google" --style-help > config/yapf.cfg

check: isort yapf

clean:
	rm -rf build

.PHONY: check clean isort yapf
