t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if(n==1 and m==1):
        print(0)
    else:
        ans = 2*min(n,m) + max(n,m)-2 
        print(ans)    