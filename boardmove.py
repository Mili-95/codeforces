t = int(input())
for _ in range(t):
    n = int(input())
 
    count = 0
    for i in range(1, int(n/2)):
        count=count+(i*i*8)
    
    print(count)    