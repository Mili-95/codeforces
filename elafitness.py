import math
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    ll = math.isqrt(l)
    rr = math.isqrt(r)
    al = 0
    ar = 0
    for i in range(3):
        if(ll * (ll + i) >= l):
            al+=1
        if(rr * (rr + i) <= r):
            ar+=1
    ans = al + 3 *(rr - ll - 1) + ar
    print(ans)            