t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    min_d = float("inf")
    for i in range(1, n):
        min_d = min(min_d, abs(a[i] - a[i-1]))
    print(min_d)    