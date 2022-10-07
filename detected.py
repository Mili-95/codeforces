list1 = None
list1_l = []
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr) - 1):
        list1 = i + 1

    if arr[0] != arr[list1]:
        if list1 == 1:
            list1_l.append(list1)
        else:
            list1 += 1
            list1_l.append(list1)
    else:
        list1_l.append(list1)


    t -= 1

for  j in list1_l:
    print(j)                    
