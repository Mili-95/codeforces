for i in [0]*int(input()):
    a,b,c=map(int, input().split())
    if b<c:b=2*c-b
    print(b>a and 1 or a>b and 2 or 3)
        
