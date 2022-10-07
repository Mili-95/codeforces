n = int(input())

for _ in range(n):
    t = int(input())
    a = t // 2
    if a % 2 != 0:
        print("NO")
        continue

    even = [2 * (i + 1) for i in range(a)]
    odd = [1 + 2 * i for i in range(a - 1)]
    result = even + odd + [sum(even) - sum(odd)]

    print("YES")
    print(*result)