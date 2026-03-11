from numpy import*
v=array(eval(input( )))
i=0

while i<size(v):
	if v[i]>=80.00:
		v[i]=v[i]-5.0
	i=i+1
	
print(round(sum(v),2))