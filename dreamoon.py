n, m = map(int, input().split())
count = 0
if m > n :
    count = -1
else:
    if (n%2==0):
        count = n / 2+1
    else:
        count =  n/2
        while(count%m!=0):
            count+=1
print(count)     
      

