import math
a = float(input())
b = float(input())
c = float(input())
dis = b**2 - 4 * a * c
if dis > 0:
    x2 = (-b + math.sqrt(dis)) / (2 * a)
    x1 = (-b - math.sqrt(dis)) / (2 * a)
    if x1 < x2:
        if x1 % 1 == 0:
            x1 = int(x1)
        if x2 % 1 == 0:
            x2 = int(x2)
        print(x1, x2,)
    else:
        print(x2, x1)
if dis == 0:
    x = -b / (2 * a)
    print(x)
