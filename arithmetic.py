t = int(input())
total = 0
for _ in range(t):
    n = int(input())
    x = [int(num) for num in input().split()]
    for i in range(n):
        total = sum(x) - n
    if (total==0):
        print(0)
    elif(total < 0):
        print(1)
    else:
        print(total)         