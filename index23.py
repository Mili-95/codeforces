height = int(input().split()[1])
h_s = input().split()
 
print(sum([(int(int(i)>height) + 1) for i in h_s]))