from sys import stdin
a, b, c = tuple(map(int, stdin.read().split()))
ans = a+b+c
ans = max(ans,(a*b*c))
ans = max(ans,(a+b)*c)
ans = max(ans,a*(b+c))
ans = max(ans,a+(b*c))
ans = max(ans,(a*b)+c)
print(ans)