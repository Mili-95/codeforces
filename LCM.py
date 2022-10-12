t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    x = 0
    y = 0
    if(l*2 <= r):
        x = l
        y = l * 2
    else:
        x = -1
        y = -1
    print(x, y)   