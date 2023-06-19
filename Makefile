###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: test clean-output yaml

COMMON_ARGS := -o $($(PROJ)_DIR) $($(PROJ)_DIR)

edit: python-edit

test: clean-output venv | $(VENV_CONC)
	$(PYTHON_BIN)/cookiecutter \
		--no-input \
		$(COMMON_ARGS)

OUTPUT := project-name

clean-output:
	rm -rf $($(PROJ)_DIR)/$(OUTPUT)

yaml: $(YAML_PREFIX)lint-local $(YAML_PREFIX)lint-manifest.yaml
