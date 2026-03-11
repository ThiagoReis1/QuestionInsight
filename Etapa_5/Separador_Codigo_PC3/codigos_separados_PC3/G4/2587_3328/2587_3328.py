from numpy import *

vel=array(eval(input("valor: ")))

l=vel[0]
ls=l+(l*0.50)
m=0

for i in range(size(vel)):
	if(vel[i]>ls):
		print(i)
		m=m+1			
print(m)