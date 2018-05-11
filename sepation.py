s = input()
entre1 = s.find('h')
entre2 = s.rfind('h')
str1 = s[entre1], s[entre2]
str2 = s[:entre1]
str3 = s[entre2+1:]
print(str2, str3, sep='')
