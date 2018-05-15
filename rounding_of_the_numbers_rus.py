import math
n = float(input())
if n % 1 < 0.5:
    print(math.floor(float(n)))
elif n % 1 >= 0.5:
    print(math.ceil(float(n)))
