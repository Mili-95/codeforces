R=lambda:map(int,input().split())
t,=R()
while t:
 t-=1;n,=R();a=sorted(y-x for x,y in zip(R(),R()));i=j=0
 while i+j+1<n:j+=a[i]+a[~j]>=0;i+=1
 print(j)