from numpy import*
v= array(eval(input("vetor")))
i=0

while (i<size(v)):
	if (v[i]>=80.00):
		v[i]=v[i] - v[i]*0.15
	i=i+1
	
print(round(sum(v),2))