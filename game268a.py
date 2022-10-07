n = int(input())
count = 0

group1 = []
group2 = []

for i in range(n):
    a, b = map(lambda k:int(k),input().split())
    group1.append(a)
    group2.append(b)


for i in group1:
    z = 0
    while z < len(group2):
        if i == group2[z]:
            count +=1
        z += 1
print(count)                       

    


