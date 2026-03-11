from numpy import*

v=array(eval(input()))

x=size(v)
i=0
y=0

while i < x:
	if(v[i]>80.0):
		v[i]=v[i]-v[i]*0.15
	y=y+v[i]
	i=i+1
i=0

print(round(y,2))