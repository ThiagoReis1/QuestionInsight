from numpy import*
x=array(eval(input("x:")))
i=0
s=0
while(i!=size(x)):
	if(x[i]>80):
		s=s+x[i]-(x[i]*0.15)
		i=i+1
	else:
		s=s+x[i]
		i=i+1
print(round(s,2))