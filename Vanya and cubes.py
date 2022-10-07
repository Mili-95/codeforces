n = int(input())
cube = layer = 0
i = 0
while cube <= n:
    layer += 1
    i += layer
    cube += i
print(layer-1)    