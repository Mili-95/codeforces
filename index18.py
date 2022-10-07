n = input()
count = 0
for digit in n:
    if digit == "4" or digit == "7":
        count = count + 1
print(count) 
a_counter = 0

for digit in str(count):
    if digit == "4" or digit == "7":
        a_count = count + 1
if a_count == len(str(count)):
    output = "YES"
else:
    output = "NO"   
print(a_count) 
print(count) 