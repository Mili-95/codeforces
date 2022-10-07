s, n = map(int, input().split())
a = map(int, input().split())
for _ in range(n):
    x,y = sorted(a)
    if s > x:
        s += y
    else:
        print("NO")
        break
print("YES")        
