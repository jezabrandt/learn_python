n = int(input())
maxn = int(input())
maxn2 = n
if n > maxn:
    maxn2 = maxn
    maxn = n
    n = int(input())
while n != 0:
        if n >= maxn:
            maxn2 = maxn
            maxn = n
        elif maxn2 < n < first:
            maxn2 = n
        n = int(input())
print(maxn2)
