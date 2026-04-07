section .data
    input: db "%d", 0
    result: db "%d", 10, 0
    
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
    
    mov ecx, 0
	
    push n
    push input
    call scanf
    add esp, 8
    
    mov edi, 1000
    sub edi, [n]
    
    mov edx, 0
    mov eax, edi
    mov edi, 500
    div edi
    mov edi, edx
    
    add ecx, eax
    
    mov edx, 0
    mov eax, edi
    mov edi, 100
    div edi
    mov edi, edx
    
    add ecx, eax
    
    mov edx, 0
    mov eax, edi
    mov edi, 50
    div edi
    mov edi, edx
    
    add ecx, eax
    
    mov edx, 0
    mov eax, edi
    mov edi, 10
    div edi
    mov edi, edx
    
    add ecx, eax
    
    mov edx, 0
    mov eax, edi
    mov edi, 5
    div edi
    mov edi, edx
    
    add ecx, eax
    
    mov edx, 0
    mov eax, edi
    mov edi, 1
    div edi
    mov edi, edx
    
    add ecx, eax
    
    push ecx
    push input
    call printf
    add esp, 8
    
    pop edi
    pop ecx
    pop ebx
    mov eax, 0
    ret