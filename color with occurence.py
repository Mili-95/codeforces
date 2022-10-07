import sys
input = sys.stdin.readline
 
INF = 10 ** 20
 
def solve():
    t = input().strip()
    T = len(t)
    dp = [INF] * (T + 1)
    word = [-1] * (T + 1)
    prev = [-1] * (T + 1)
    dp[0] = 0
 
    a = []
    N = int(input())
    for _ in range(N):
        s = input().strip()
        a.append(s)
 
    for start in range(T):
        for k, s in enumerate(a):
            L = len(s)
            if start + L <= T and t[start:start + L] == s:
                for i in range(1, L + 1):
                    if dp[start + i] > dp[start] + 1:
                        dp[start + i] = dp[start] + 1
                        prev[start + i] = start
                        word[start + i] = k
 
    if dp[T] >= INF:
        print(-1)
        return
    print(dp[T])
 
    ans = []
    current = T
    while prev[current] != -1:
        ans.append((word[current] + 1, prev[current] + 1))
        current = prev[current]
 
    for pair in ans:
        print(str(pair[0]) + " " + str(pair[1]))
 
T = int(input())
for _ in range(T):
    solve()