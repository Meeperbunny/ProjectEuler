.PHONY: run create

run:
	@if [ -z "$(file)" ]; then \
		echo "Error: No filename provided. Please supply file=<filename>"; \
		exit 1; \
	fi
	@g++ $(file) -g -Wall -Wextra -Wfatal-errors -DIAN_DEBUG -o source.exe -O3 -std=c++2a
	@./source.exe
	@rm -f source.exe

create:
	@target=$(word 2,$(MAKECMDGOALS)); \
	if [ -z "$$target" ]; then \
		echo "Usage: make create <number>"; exit 1; \
	fi; \
	cp scripts/template.cc scripts/$$target.cc; \
	echo "Created scripts/$$target.cc from scripts/template.cc"

# Dummy rule to avoid errors with additional arguments
%:
	@:
