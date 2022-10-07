t = int(input())
for _ in range(t):
    n = int(input())
    weight = [int(i) for i in input().split()]
    if sum(weight) % 2 != 0:
        print("NO")
        continue
    c1, c2 = 0, 0
    for i in range(n):
        if weight[i] == 1:
            c1 += 1
        elif weight[i] == 2:
            c2 += 1
    if c2 % 2 != 0:
        if c1 == 0:
            print("NO")
            continue
    print("YES")                 