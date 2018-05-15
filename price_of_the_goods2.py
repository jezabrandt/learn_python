import math
n = float(input())
x = n % 1
x2 = round(x, 6)
x1 = math.floor(float(n))
print(x1, int(x2 * 100))
