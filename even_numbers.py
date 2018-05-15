a = int(input())
b = int(input())
c = int(input())
if a == 0 and b == 0 and c == 0:
    print('NO')
elif a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print('YES')
else:
    print('NO')
