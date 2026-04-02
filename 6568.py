import sys
import math

input = sys.stdin.read
sys.setrecursionlimit(1000000)

ins = input().rstrip().rsplit()
inlen = len(ins)

def bintonum_5(string):
    ing = list(map(int, list(string)))
    return ing[0] * 16 + ing[1] * 8 + ing[2] * 4 + ing[3] * 2 + ing[4] * 1

def add_alu(alu):
    alu += 1
    if alu > 255:
        alu = 0
    return alu

def min_alu(alu):
    alu -= 1
    if alu < 0:
        alu = 255
    return alu

for T in range(0, inlen//32):
    commands = ins[32*T:32*T+32]
    pc = 0
    alu = 0
    while True:
        cur = commands[pc]
        pc = (pc + 1) % 32
        cmd = cur[:3]
        if cmd == "000":
            x = int(cur[3:], 2)
            commands[x] = f"{alu:08b}"
        elif cmd == "001":
            x = int(cur[3:], 2)
            alu = int(commands[x], 2)
        elif cmd == "010":
            x = int(cur[3:], 2)
            if alu == 0:
                pc = x
        elif cmd == "100":
            alu = min_alu(alu)
        elif cmd == "101":
            alu = add_alu(alu)
        elif cmd == "110":
            x = int(cur[3:], 2)
            pc = x
        elif cmd == "111":
            break
        if pc >= 32:
            break
    print(f"{alu:08b}")