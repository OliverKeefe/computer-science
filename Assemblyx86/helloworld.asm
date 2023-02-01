section .date
    msg db 'Hello, World!', 0

section .text
    global _start

_start:
    ; write the string to stdout
    mov eax, 4 ; system call number (sys_write)
    mov ebx, 1 ;
    mov ecx, msg ; pointer to message
    mov edx, 13 ; length of the message
    int 0x80 ; call kernel

    ; exit gracefully
    mov eax, 1 ; system call number (sys_ext)
    xor ebx, edx ; exit code (0)
    int 0x80 ; call kernel