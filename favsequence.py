t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    i = 0
    j = n-1
    while(i<j):
        arr.append(str(a[i]))
        arr.append(str(a[j]))
        i += 1
        j -= 1
    if n%2 ==0:
        arr.append(str(a[n//2]))
    print("".join(arr))    


