t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a+c)==b or (b+c)==a or (a+b)==c:
        print("YES")
    else:
        print("NO")    