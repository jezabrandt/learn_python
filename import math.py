import math
a = float(input())
b = float(input())
c = float(input())
di = b ** 2 - 4 * a * c
if di > 0:
    x1 = (-b + math.sqrt(di)) / (2 * a)
    x2 = (-b - math.sqrt(di)) / (2 * a)
elif di == 0:
    x = -b / (2 * a)
    print(x)
else:
    print()
if di > 0 and x1 < x2:
        print(x1, x2)
else:
        print(x2, x1)
