t = int(input())
for _ in range(t):
    a, b = input().split()
    if a == b:
        print("=")
    else:
        if a[len(a)-1]==b[len(b)-1]:
            if a[(len(a))-1] =='S':
                if len(a)>len(b):
                    print("<")
                else:
                    print(">")
            elif a [(len(a))-1]=="L":
                if len(a) > len(b):
                    print(">")
                else:
                    print("<")
            else:
                print("=")
        else:
            if a[(len(a))-1]=='S':
                print("<")
            elif a[(len(a))-1]=='M':
                if b[(len(b))-1]=='S':
                    print(">")
                else:
                    print("<")
            else:
                print(">")                

