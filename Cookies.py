n = input()
bags = map(int, input().split())
ways = 0
if sum(bags) % 2 == 0:
    for bag in bags:
        if bag % 2 == 0:
            ways += 1
else:
    for bag in bags:
        if bag % 2 != 0:
            ways += 1
print (ways)