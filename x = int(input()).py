x = int(input())
i = 2
while i < x:
    if x % i ==0:
        answer = i
        i = x
    else:
        i = i + 1 
print(answer)

