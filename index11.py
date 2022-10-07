num = int(input())
l1 = list(input())
tot = 1
for i in range(num-1):
    if l1[i]==l1[i+1]:
        tot+=1
print(tot-1)