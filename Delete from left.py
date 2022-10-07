s = input()
t = input()
sl=len(s)
tl=len(t)
while sl and tl and s[sl-1]==t[tl-1]:
    sl-=1
    tl-=1
print(sl+tl)