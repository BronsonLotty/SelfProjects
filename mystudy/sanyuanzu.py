X = int(input())
Y = int(input())
Z = int(input())
n = min(X,Y,Z)


for a in range(1,X+1):
    for b in range(1,Y+1):
        if b == a:
            continue
        for c in range(1,Z+1):
            if c == a or c == b:
                continue
            if a < (b + c) and b < (a + c) and c < (a + b):
                n = n + 1

for a in range(1,X+1):
    if a in range(1, Y+1):
        b = a
        for c in range(1, Z+1):
            if c == a:
                continue
            if a < (b + c) and b < (a + c) and c < (a + b):
                n = n + 1
    else:
        break

for a in range(1,X+1):
    if a in range(1,Z+1):
        c = a
        for b in range(1, Y+1):
            if b == a:
                continue
            if a < (b + c) and b < (a + c) and c < (a + b):
                n = n + 1
    else:
        break

for b in range(1, Y+1):
    if b in range(1, Z+1):
        c = b
        for a in range(1,X+1):
            if a == b:
                continue
            if a < (b + c) and b < (a + c) and c < (a + b):
                n = n + 1

print(n)