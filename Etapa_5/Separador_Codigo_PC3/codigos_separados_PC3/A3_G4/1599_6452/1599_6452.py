from numpy import*
v=array(eval(input('digite o vetor: ')), dtype=float)
i=0
vtot=0
while i<size(v):
	if v[i]>80:
		v[i]=v[i]-0,15*v[i]
	i=i+1
vtot=sum(v)
print(round(vtot,2))
	
	