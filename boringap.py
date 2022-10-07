t = int(input())

for _ in range(t):
    n = input()
    num = len(n)
    count = 0
    for i in range(1, int(n[0])):
        count += 10
    for i in range(1, num+1):
        count += i
    print(count)        