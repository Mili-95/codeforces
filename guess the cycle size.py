for i in range(25):
    print('?',1,1+i+1)
    x=int(input())
    if x==-1:
        print('!',1+i)
        break
    print('?',2+i,1)
    y=int(input())
    if x!=y:
        print('!',x+y)
        break