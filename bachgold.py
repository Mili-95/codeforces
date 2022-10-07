n = int(input())
prime = []
if n % 2 == 1:
    prime.append(3)
    n -= 3
for _ in range(n, 0, -2):
    prime.append(2)

print(len(prime))
for i in range(len(prime)):
    print(prime[i], end =" ")        
