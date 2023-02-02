secion .data
f1 dd 3.14
f2 dd 2.718

section .text
    global _start

_start:
    fld dword [f1]
    fld dword [f2]
    fmulp
    fstp
    fstp dword [result]

    ; exit program gracefully
    mov eax, 1
    xor ebx, ebx
    int 0x80