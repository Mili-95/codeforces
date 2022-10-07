n = int(input())

welf = list(map(int, input().split()))

equ = max(welf)
s = sum(equ - w for w in welf)

print(s)
