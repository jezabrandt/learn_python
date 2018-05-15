amount = int(input())
if (amount % 10 == 1) and amount != 11:
    print(amount,  'korova')
elif (2 <= (amount % 10) < 5) and amount not in [12, 13, 14]:
    print(amount, 'korovy')
else:
    print(amount, 'korov')
