t = int(input())
for _ in range(t):
    w, h, n = [int(i) for i in input().split()]
    if n == 1:
        print("YES")
        continue
    count = 1
    while w % 2 == 0:
        count *= 2
        w //= 2
    while h % 2 == 0:
        count *= 2
        h //= 2
    if count >= n:
        print("YES")
    else:
        print("NO")            