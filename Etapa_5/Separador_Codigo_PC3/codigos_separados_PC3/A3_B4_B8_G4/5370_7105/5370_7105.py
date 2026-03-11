from numpy import *
i = 0
aux = 0
cont=0
v = eval(input())

while(i<size(v)):
	if(i==0):
		aux = v[i]
		cont+=1
	else:
		if(v[i]>aux):
			aux = v[i]
			cont +=1
	i+=1

if(size(v) == cont):
	print("True")
else:
	print("False")