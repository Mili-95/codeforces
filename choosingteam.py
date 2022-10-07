n, c = map(int, input().split())

participated = map(int, input().split())

ans = sum(1 for p in participated if 5 - p >= c) // 3
print(ans)