def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        e1 = a - 1
        e2 = abs(b - c) + c - 1
        count = 0
        if e1 <= e2:
            count += 1 
        if e1 >= e2:
            count += 2
        print(count) 
main()                 