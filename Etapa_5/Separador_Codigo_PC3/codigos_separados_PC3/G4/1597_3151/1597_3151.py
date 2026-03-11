from numpy import*
v=array(eval(input()))
i=0
while(i<len(v)):
	if(v[i]>80):
		v[i]=v[i]-5    
		i=i+1
	else:
		v[i]=v[i]+0
		i=i+1
print(round(sum(v),2))
