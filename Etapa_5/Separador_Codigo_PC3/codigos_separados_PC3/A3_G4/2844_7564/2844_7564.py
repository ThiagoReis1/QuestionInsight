from numpy import*
v=array(eval(input("")))
v1=0
for i in range (size(v)):
	v[i]=v[i]-1
	if(v[i]<0):
		v[i]=9
	
print(v)