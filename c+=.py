t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    sum = 0
    count = 0
    while sum <= n:
        if a > b:
            b += a
            sum = b
            count+=1
        else:
            a += b
            sum = a
            count+=1
       
    print(count)        

   




