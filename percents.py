import math
p = int(input())
x = int(input())
y = int(input())
p1 = p / 100
x1 = (x * p1 + x) + (y * p1 + y)
dep2 = x1 % 1
dep = round(dep2, 6)
depY = int(dep * 100)
depX = math.floor(float(x1))
