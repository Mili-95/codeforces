input1 = input()
input2 = input()

math = []
for i,x in enumerate(input1):
    if x == input2[i]:
        math.append("0")
    else:
        math.append("1")
result = "".join(math)
print(result)            