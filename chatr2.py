s = input()
l = 'hello'
count = -1
for i in range(len(s)):
    count = s.find(i, count + 1)
    if count == -1:
        print('NO')
    else:
        print('YES')        
    