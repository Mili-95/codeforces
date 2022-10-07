"""you can find a first two string, inside the below five strings array list
first input index match to list array index"""
s = input()
card = input().split()
count = 0
for i in card:
    if (i[0]==s[0] or i[1]==s[1]):
        count = 1

if count:
    print("YES")
else:
    print("NO")               
    

    


