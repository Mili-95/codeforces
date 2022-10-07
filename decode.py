for s in[*open(0)][2::2]:
 *s,=s[:-1];r=''
 while s:
  if(x:=s.pop())<'1':x=s[-2]+s[-1];s[-2:]=[]
  r=chr(96+int(x))+r
 print(r)