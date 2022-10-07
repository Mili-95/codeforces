from itertools import count


t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    if n < 2:
        print(1)
        continue
    else:
        count = 1
        if(n-2)%x == 0:
            count += (n-2) // x
        else:
            count += (n-2) // x+1
        print(count)        