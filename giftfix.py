t = int(input())

for  _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    x, y = min(a), min(b)
    count = 0
    for i in range(n):
        count += max(a[i]-x, b[i]-y)
    print(count)    