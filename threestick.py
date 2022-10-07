t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = sorted(a)
    ans = 3*x[-1]
    for i in range(1, n-1):
        ans = min(ans, x[i+1]-x[i-1])
    print(ans)    
    