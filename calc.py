a = float(input())
b = float(input())
c = input()
if c == 'mod':
    print(a % b)
    iif b == 0:
    print('Деление на 0!')
if c == 'div':
    print(a // b)
    if b == 0:
    print('Деление на 0!')
if c == 'pow':
    print(a ** b)
if c == '-':
    print(a - b)
if c == "+":
    print(a + b)
if c == '*':
    print(a * b)
if c == '/':
    print(a / b)
    if b == 0:
    print('Деление на 0!')




    A = float (input())
B = float (input())
C = str (input())
if C =='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/' and B==0:
    print("Деление на 0!")
elif C=='/' and B!=0:
    print(A/B)
elif C=='mod' and B==0:
    print('Деление на 0!')
elif C=='mod' and B!=0:
    print(A%B)
elif C=='pow':
    print(A**B)
elif C=='div' and B==0:
    print('Деление на 0!')
elif C=='div' and B!=0:
    print(A//B)

