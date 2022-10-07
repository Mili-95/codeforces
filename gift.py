n = int(input())
g = [*map(int,input().split())]
for i in range(n):
    print(*[g.index(i+1)+1])

   




