from numpy import *
v1=array(eval(input()))
i=0
cont=0
while(i<size(v1)):
	if(v1[i]>=0):
		cont=cont+1
	i=i+1
v2=array(zeros(cont,dtype=float))
i=0
j=0
while(j<size(v1)):
	if(v1[j]>=0):
		v2[i]=v1[j]
		i=i+1	
	j=j+1	
print(v2)

	
