t = int(input())
for _ in range(t):
    s = input()
    a = 0
    b = 0
    c = 0
    for i in s:
        if(i == "A"):
            a+=1      
        elif(i == "B"):
            b+=1       
        elif(i == "C"):
            c+=1
    if(a+c == b):
        print("YES")   
    else:
        print("NO")

"""main logic if i want delete "AB" or "BC",  "CB". then
B must be delete in any situation.  if "a" value or "c" value equal to "b"
 value then I erase the full string neither not a+c == b .
"""
