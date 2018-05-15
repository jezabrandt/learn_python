n = int(input())
lenght = 0
sumSeq = 0
while n != 0:
    lenght += 1
    sumSeq += n
    n = int(input())
print(sumSeq / lenght)
