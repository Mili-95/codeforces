from itertools import count


n = int(input())

counter = 0

for _ in range(n):
    p,q = map(int, input().split())
    if(q - p) >= 2:
        counter = counter + 1
print(counter)        