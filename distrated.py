t = int(input())

for _ in range(t):
    n = int(input())
    task = input()
    visit = []
    flag = 0
    for i in range(1, n):
        if task[i] != task[i-1]:
            if task[i-1] not in visit:
                visit.append(task[i-1])
            else:
                flag = 1
                break
    if flag == 0 and task[-1] not in visit:
        print("YES")
    else:
        print("NO")                