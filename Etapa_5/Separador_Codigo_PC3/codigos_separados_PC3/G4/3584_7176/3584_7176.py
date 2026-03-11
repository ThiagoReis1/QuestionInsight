from numpy import*
v=array(eval(input("vetor:")))
n=0
x=0
while(size(v)>n):
	if(v[n]>200):
		x=x+v[n]-(v[n]*0.15)
		n=n+1
	else:
		x=x+v[n]
		n=n+1
print(round(x,2))