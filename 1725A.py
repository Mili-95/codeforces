n,m= map(int,input().split())
ans=0
if m>1:
    ans=(m-1)*n
else:
    ans=n-1
print(ans)