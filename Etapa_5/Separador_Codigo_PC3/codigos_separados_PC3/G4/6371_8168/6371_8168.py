from numpy import *
v=array(eval(input("")))

vz=zeros(size(v),dtype=int)
i=0
for x in v:
	if(x!=0):
		vz[i]= (x-1)**2
	else:
		vz[i]=81
	i+=1
print(vz)