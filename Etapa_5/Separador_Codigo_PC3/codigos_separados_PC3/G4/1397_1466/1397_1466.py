a=int(input())
if(a>10000):
	t= 10000*5 + (a-10000)*4
else:
	t=a*5
print(round(t,2))