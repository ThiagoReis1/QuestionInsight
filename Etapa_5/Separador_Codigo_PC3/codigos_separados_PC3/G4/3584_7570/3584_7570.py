from math import*
from numpy import*
x = array(eval(input("")))
i = 0
c=0
while(i<size(x)):
	if(x[i]>200 ):
		c=c+ x[i]-(x[i]*0.15)
	else:
		c=c+x[i]
	i=i+1
print(round(c,2))