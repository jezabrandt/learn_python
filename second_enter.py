s = input()
pos = 0
for i in range(len(s)):
    if s[i] == 'f':
        pos += 1
        if pos == 2:
            print(i)
if pos == 1:
    print('-1')
elif 'f' not in s:
    print('-2')
