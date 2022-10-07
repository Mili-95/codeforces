n = int(input())
point = list(map(int, input().split()))
count = 0
for i in range(1, n):
    maxi = 0
    mini = 0
    for a in range(0, i):
        if point[i] > point[a]:
            maxi = maxi + 1
        elif point[i] < point[a]:
            mini = mini + 1
    if maxi == i or mini == i:
        count = count + 1
print(count)              






