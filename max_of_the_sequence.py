n = int(input())
maxn = n
while n != 0:
    if maxn < n:
        maxn = n
    n = int(input())
print(maxn)
