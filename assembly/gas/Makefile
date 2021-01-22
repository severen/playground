# This Makefile is written specifically for GNU Make in a Linux environment.

BUILD_DIR := build

SRCS := $(wildcard *.s)
PROGS := $(patsubst %.s, $(BUILD_DIR)/%, $(SRCS))

.PHONY: all
all: $(PROGS)

.PHONY: clean
clean:
	rm -r $(BUILD_DIR)

$(BUILD_DIR)/%: $(BUILD_DIR)/%.o
	ld -m elf_x86_64 -o $@ $<
$(BUILD_DIR)/%.o: %.s | $(BUILD_DIR)/
	as -64 -o $@ $<

$(BUILD_DIR)/:
	mkdir -p $@
