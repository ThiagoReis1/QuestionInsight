from numpy import*
v=array(eval(input()))
i=0
while i<size(v):
	if v[i]>=80.0:
		v[i]=v[i]*0.85
	i=i+1
	
print(round(sum(v),2))
		
		