x, y = [int(i) for i in input().split()]
mx = max(x, y)
count = 0
for i in range(1, 7):
    if i >= mx:
        count += 1
if count == 6:
    print("1/1")
elif count % 2 and count != 3:
    print("%s/%s" % (count, 6))
else:
    if count == 3:
        print("1/2")
    else:
        print("%s/%s" % (count // 2, 3))                    