for t in range(int(input())):
    n=int(input()); arr=[]
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    for i in range(n): arr.append(y[i]-x[i])
    arr.sort(); res=0
    l=0; r=n-1
    while l<r:
        if arr[l]+arr[r] >= 0: res+=1; r-=1
        l+=1
    print(res)