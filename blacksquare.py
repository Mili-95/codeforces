a,b,c,d = [int(i) for i in input().split()]
s = input()
res = 0
for i in range(len(s)):
    if s[i] == "1":
        res += a
    elif s[i] == "2":
        res += b
    elif s[i] == "3":
        res += c
    elif s[i] == "4":
        res += d
print(res)                    