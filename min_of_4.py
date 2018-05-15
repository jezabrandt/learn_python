def min4(a, b, c, d):
    return min(min(a, b), min(d, c))
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
