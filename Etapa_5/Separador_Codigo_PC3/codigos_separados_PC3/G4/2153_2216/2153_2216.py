from numpy import * 
v1=array(eval(input("vetor 1")))
v2= array(eval(input("vetor 2")))
d=0
for i in range(size (v2)):
	d += (v1[i]-v2[i])**2


print(round(d**(1/2),4))