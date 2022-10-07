t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if l[i] & 1:
            count += 1
    if (count%4 == 0 or count%4 == 3):
        print("Alice")
    elif count%4 == 2:
        print("Bob")
    else:
        if n & 1:
            print("Bob")
        else:
            print("Alice")                    
       