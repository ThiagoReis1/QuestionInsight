from numpy import *
v=array(eval(input("")))
acu=0
y=0
i=0

for x in v:
	if(x%5==0):
		acu +=1
vz=zeros(acu,dtype=int)
print(acu)

for x in v:
	if(x%5==0):
		vz[y]=i
		y+=1
	i+=1
print(vz)