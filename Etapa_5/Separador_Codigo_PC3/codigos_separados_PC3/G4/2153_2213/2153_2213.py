from numpy import *
p=array(eval(input(":")))
q=array(eval(input(":")))
d=0
for i in range(size(q)):
	d+=(p[i]-q[i])**2
print(round(sqrt(d),4))