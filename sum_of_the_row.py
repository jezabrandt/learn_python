n = int(input())
sumn = 0
for i in range(1, n + 1):
    a = (1 / i ** 2)
    sumn += a
if sumn % 2 == 0:
    print(int(sumn))
else:
    print('{0:.6f}'.format(sumn))
