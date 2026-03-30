section .data
    input: db "%d", 0
    output: db "*", 0
    wn: db 10, 0

section .bss
    n: resd 1

section .text
    global main
    extern scanf
    extern printf

main:
    push ebx
    push ecx
	
    push n
    push input
    call scanf
    add esp, 8
    
    mov ebx, [n]
    
    _iloop:
        mov esi, ebx
        _jloop:
            push output
            call printf
            add esp, 4
            dec esi
            cmp esi, 0
            jne _jloop
        push wn
        call printf
        add esp, 4
        dec ebx
        cmp ebx, 0
        jne _iloop
    
    pop ecx
    pop ebx
    mov eax, 0
    ret
