from math import *
n=int(input("n:"))
t=1
i=1
soma=-(1/9)
r=5
f=2
while(t<n):
	soma=soma+((i*(sqrt(f)))/(6+r))
	r=r+2
	t=t+1
	i=i*-1
	f=f+1
print(round(soma,5))
	
	