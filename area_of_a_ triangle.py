a = float(input())
b = float(input())
c = float(input())
p = a + b + c
d = p/2

s = (d*(d-a)*(d-b)*(d-c))**0.5
if s % 2 == 0:
    print(int(s))
else:
    print('{0:.6f}'.format(s))
