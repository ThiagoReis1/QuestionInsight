from numpy import *
v=array(eval(input("")))
i=0
peso=0
total=0
while (i<size(v)):
	total=total+v[i]*(i+1)
	peso=peso+(i+1)
	i=i+1
print(round(total/peso,2))