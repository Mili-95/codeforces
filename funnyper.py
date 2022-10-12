t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
    else:
        for i in range(n):
            if (i<n//2):
                print(n-i, end=" ")
            else:
                print(i-n//2+1, end =" ")
