t = int(input())
""""main logic is that if i want odd then ,an array have to an odd and even,
then their sum will be odd, one odd is enough to get in result an odd"""
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    sum = 0
    for i in range(n):
        if a[i]%2 !=0 or a[i]==1:
            odd+=1
        else:
            even+=1
        sum+=a[i]
    if sum%2 !=0 or sum==1:
        print("YES")
    else:
        if(odd!=0 and even!=0):
            print("YES")
        else:
            print("NO")        


