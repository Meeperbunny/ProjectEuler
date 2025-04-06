.PHONY: run create

# Detect platform and set compiler
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    CXX := clang++
else
    CXX := g++
endif

# Compiler flags
CXXFLAGS := -I ~/include -std=c++2a -g -Wall -Wextra -Wfatal-errors -DIAN_DEBUG -O3 -march=native

# Run the provided file: make run file=scripts/208.cc
run:
	@if [ -z "$(file)" ]; then \
		echo "Error: No filename provided. Use: make run file=<filename>"; \
		exit 1; \
	fi
	@$(CXX) $(CXXFLAGS) $(file) -o source.exe
	@./source.exe
	@rm -f source.exe

# Create a new file: make create name=208
create:
	@if [ -z "$(name)" ]; then \
		echo "Error: No name provided. Use: make create name=<number>"; \
		exit 1; \
	fi
	@cp scripts/template.cc scripts/$(name).cc
	@echo "Created scripts/$(name).cc from template."

# Dummy rule to absorb extra args
%:
	@:
