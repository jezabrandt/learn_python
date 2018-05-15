n = int(input())
lenCur = 1
lenmax = 0
prew = -1
while n != 0:
    if prew == n:
        lenCur += 1
    else:
        prew = n
        lenmax = max(lenmax, lenCur)
        lenCur = 1
    n = int(input())
lenmax = max(lenmax, lenCur)
print(lenmax)
