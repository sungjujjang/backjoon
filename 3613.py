import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

varname = input().rstrip()

if not varname:
    print("Error!")
    exit()

has_underscore = "_" in varname
has_upper = any(c.isupper() for c in varname)

if has_underscore and has_upper:
    print("Error!")
    exit()

if not has_underscore and not has_upper:
    print(varname)
    exit()

if "_" in varname:
    ctn = False
    result = ""

    if varname[0] == "_" or varname[-1] == "_":
        print("Error!")
        exit()

    for i in range(len(varname)):
        if ctn:
            ctn = False
            continue

        if varname[i].isupper():
            print("Error!")
            exit()

        if varname[i] == "_":
            if varname[i+1] == "_" or varname[i+1].isupper():
                print("Error!")
                exit()
            result += varname[i+1].upper()
            ctn = True
        else:
            result += varname[i]

else:
    result = ""

    if varname[0].isupper():
        print("Error!")
        exit()

    for v in varname:
        if v.isupper():
            result += "_" + v.lower()
        else:
            result += v

print(result)
