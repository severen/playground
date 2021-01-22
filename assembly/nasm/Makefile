# This Makefile is written specifically for GNU Make in a Linux environment.

BUILD_DIR := build

SRCS := $(wildcard *.asm)
PROGS := $(patsubst %.asm, $(BUILD_DIR)/%, $(SRCS))

.PHONY: all
all: $(PROGS)

.PHONY: clean
clean:
	rm -r $(BUILD_DIR)

$(BUILD_DIR)/%: $(BUILD_DIR)/%.o
	ld -m elf_x86_64 -o $@ $<
$(BUILD_DIR)/%.o: %.asm | $(BUILD_DIR)/
	nasm -f elf64 -o $@ $<

$(BUILD_DIR)/:
	mkdir -p $@
