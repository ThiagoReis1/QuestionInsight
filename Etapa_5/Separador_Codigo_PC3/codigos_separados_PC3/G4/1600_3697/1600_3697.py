from numpy import*
c=array(eval(input()))
i=0
p=0
while(i<size(c)):
	if(c[i]>80.0):
		p=p+ c[i]*0.85
		i=i+1
	else:
		p=p+c[i]
		i=i+1
print(round(p,2))	