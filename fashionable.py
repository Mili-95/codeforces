"""main logic there is a 12-side polygon: if input % is 4 then yes neither no"""
t = int(input())
for _ in range(t):
    n = int(input())
    print("YES") if n % 4 == 0 else print("NO")
        
