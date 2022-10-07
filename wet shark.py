n = int(input())
all = tuple(map(int, input().split()))
s = sum(all)
 
if s%2 == 0:
    print(str(s))
else:
    min_odd = min([i for i in all if i%2==1])
    print(str(s-min_odd))