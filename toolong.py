n = int(input())
for i in range(n):
    s = str(input())
    if len(s) > 10:
        print(s[0] + str(len(s[1:-1])) + s[-1])
    else:
        print(s)    


   









   