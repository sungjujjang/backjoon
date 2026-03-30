section .data
    input: db "%d", 0
    star: db "*", 0
    blank: db " ", 0
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
    push edi
	
    push n
    push input
    call scanf
    add esp, 8
    
    mov ebx, [n]
    
    _iloop:
        mov esi, ebx
        dec esi
        _jloop:
            cmp esi, 0
            jle _nxt2
            push blank
            call printf
            add esp, 4
            dec esi
            cmp esi, 1
            jge _jloop
        _nxt2:
            mov esi, ebx
            mov edi, [n]
            inc edi
            sub edi, ebx
            add edi, edi
            dec edi
            _jloop2:
                push star
                call printf
                add esp, 4
                dec edi
                cmp edi, 1
                jge _jloop2
            _nxt1:
                push wn
                call printf
                add esp, 4
                dec ebx
                cmp ebx, 1
                jge _iloop
    
    pop edi
    pop ecx
    pop ebx
    mov eax, 0
    ret