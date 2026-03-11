from numpy import*

v = array(eval(input(":")))
i = 0


while(i<size(v)):
	if(v[i]>80):
		d = v[i]*0.15
		v[i]= v[i]-d
	i = i+1
	
print(round(sum(v),2))