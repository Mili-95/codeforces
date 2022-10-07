t = int(input())
"""two number same, those two number would be greater"""

for _ in range(t):
    x, y, z = map(int, input().split())
    if (x > y):
        (x, y) = (y, x)
    if (x > z):
        (x, z) = (z, x)
    if(y > z):
        (y, z) = (z, y)
    if( y != z):
        print("NO")
       
    else:
        print("YES")   
        print(x, x, z)               