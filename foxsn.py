n, m = map(int, input().split())
for i in range(1, n+1):
    if i % 2:
        print("#" * m)
    else:
        x = divmod(i, 4)
        if (x)[1] == 2:
            print("."*(m-1)+"#")
        else:
            print("#" + "."*(m-1))        





