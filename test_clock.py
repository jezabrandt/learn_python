v = int(input())
H = v // 3600
M = (v % 3600) // 60
S = (v % 3600) % 60
b = H / 24
if b == int(b) and b > 0:
    H = 0
elif H > 24:
    H = H - 24 * (H // 24)
if M < 10:
    M = "0" + str(M)
if S < 10:
    S = "0" + str(S)
print(H, ":", M, ":", S, sep="")
