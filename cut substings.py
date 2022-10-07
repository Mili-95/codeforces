#import io,os
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
M = 10**9+7
 
 
 
 
def main(t):
 
    M = 10**9 + 7
 
 
    s1 = input()
    s2 = input()
 
 
    n = len(s1)
    m = len(s2)
 
 
    occur = []
    for i in range(n-m+1):
        if s1[i:i+m]==s2:  
            occur.append(i)
 
#    print(occur)
 
    if len(occur)==0:
        print(0,1)
        return 
 
#    print(occur)
    
    times = 1
    M = 10**9 + 7
 
    mind = m
    for i in range(len(occur)-1):
        mind = min(mind, occur[i+1]-occur[i] )
 
    maxcover = 1 + (m - 1)//mind*2
    maxlength = (m - 1)//mind + 1
#    print(maxlength,"max")
 
 
    dp = [[0 for rest in range(n+1)] for spaces in range(n+2)]
    for rest in range(maxlength):
        dp[1][rest] = 1
    for spaces in range(2,n+2):
        dp[spaces][0] = 1
        for rest in range(1,n+1):
            for cut in range(maxlength):
                if cut > rest:  break
                dp[spaces][rest] += dp[spaces-1][rest-cut]
                dp[spaces][rest] %= M
 
 
 
#    print(dp)
 
 
 
    def getnums(p,q):   #  p is tot length and q is max cover
 
#        print(p,q,"///")
        spaces = (p - 1)//q + 2
        tot = p - (spaces - 1)* (q//2+1) + q//2 
 
#        print(spaces,tot,"**")
        return dp[spaces][tot]
 
 
 
 
 
 
 
 
 
 
 
 
    times = 0
    ans = 1
   
    count = 1
    flag = True
 
    for i in range(1,len(occur)):
        if occur[i] - occur[i-1] < m:
            count += 1
        else:
            times += (count - 1)//maxcover + 1
            ans *= getnums(count,maxcover)
            ans = ans % M
            count = 1
#        print(ans)
 
#    print("**",count)
    times += (count - 1)//maxcover + 1
    ans *= getnums(count,maxcover)
    ans = ans % M
 
 
        
 
    print(times,ans)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T = int(input())
t = 1
while t<=T:
    main(t)
    t += 1