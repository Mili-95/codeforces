"""main logic is at first found the boxes minimum value and then 
pick i candies in every boxes and count it"""

t = int(input())
for _ in range(t):
    n = int(input())
    box = list(map(int, input().split()))
    mini = min(box)
    ans = 0
    for i in box:
        ans += (i - mini)
    print(ans)    