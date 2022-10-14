t = int(input())
for _ in range(t):
     count = 0
     grid = []
     while count < 8:
        n = input()
        if len(n) != 0:
            count+=1
            grid.append(n)
     ans = False
     for i in range(8):
        x = False
        for j in range(8):
            if grid[i][j]!='R':
                x = True
        if not x:
            print('R')
            ans = True
            break
     if not ans:
        print('B')


