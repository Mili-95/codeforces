for x in range(int(input())):
	a,b=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	if l[-1]-l[0]>2*b:print(-1)
	else:print(l[0]+b)