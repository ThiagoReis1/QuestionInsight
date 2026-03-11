from numpy import*
v=array(eval(input()))
c=0

while(c < size(v)):
	if(v[c]>80):
		v[c]= v[c] - v[c]*(15/100)
	c=c+1
	
v1=sum(v)
print(round(v1,2))