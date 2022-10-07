for i in range(2,27):
 print('?',1,i);a=int(input());print('?',i,1);b=int(input())
 if a!=b:
  print('!',a+b)
  break
 elif a==-1:
  print('!',i-1)
  break