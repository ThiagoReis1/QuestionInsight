from numpy import*
v=array(eval(input("v:")))
validos=0
i=0
while(i<size(v)):
	if(v[i]<=50):
		validos=validos+1
	i=i+1
v1=ones(validos,dtype=float)
i=0
j=0
while(i<size(v)):
	if(v[i]<=50):
		v1[j]=v[i]
		j=j+1
	i=i+1
print(v1)
		