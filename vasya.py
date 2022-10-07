a, b = list(map(int, input().split()))
if a == b:
    print("%s %s" % (a, 0))
else:
    min_socks = min(a, b)
    max_socks = max(a, b)
    t = max_socks - min_socks
    print("%s %s" % (min_socks, t // 2))    