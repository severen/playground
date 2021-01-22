;; vim: ft=nasm:

;; DESCRIPTION
;;   hello - say hello!
;; SYNOPSIS
;;   hello
;; BUILDING
;;   $ nasm -f elf64 hello.asm
;;   $ ld -m elf_x86_64 -o hello hello.o
;;
;; Note that this program is written in Intel-syntax assembly for the Netwide
;; Assembler (NASM) and an x86_64 Linux environment.

; Place _start in the object code's symbol table for ld to recognise when
; linking. By default, ld requires that the main entry point be labelled
; _start.
global _start

; The text section contains executable data, i.e. instructions.
section .text
_start:
  ;;
  ;; write(1, message, message.len) system call
  ;;
  ; Specify system call no. 1, which is the code for print.
  mov rax, 1
  ; Set the file descriptor parameter to 1, which is standard output.
  mov rdi, 1
  ; Set the buffer parameter to the address of the message string.
  mov rsi, message
  ; Set the length parameter to the length of the message string in bytes.
  mov rdx, message.len
  ; Invoke the system call. The instruction `int 0x80` can also be used, but
  ; different registers will have to be used for the parameters. On x86_64
  ; Linux, `syscall` is preferred because it is faster and portable (between
  ; Intel and AMD processors). See:
  ; en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux
  syscall

  ;;
  ;; exit(0) system call
  ;;
  ; Specify system call no. 60, which is the code for exit.
  mov rax, 60
  ; Set the exit code parameter to 0, which is the code for success. Note that
  ; `xor rdi, rdi` is a (supposedly) faster method of zeroing a register than
  ; the naive method of `mov rdi, 0`.
  xor rdi, rdi
  ; Invoke the system call.
  syscall

; The rodata section contains read only non-executable data, i.e. constants.
section .rodata
; The '10' here is the ASCII code for \n.
message: db "Hello, world!", 10
; Calculate the length of the string by subtracting the current address (which
; is one past the end of the string) with the address of the first character in
; the string.
.len: equ $ - message
