for i in range(int(input())):
  a=int(input())
  b=list(map(int,input()))
  b=b[::-1]
  j=0
  num=''
  while j<a:
    if(b[j]>0):
      num+=chr(96+b[j])
      j+=1
    else:
      num+=chr(96+b[j+1]+10*b[j+2])
      j+=3
  print(num[::-1])