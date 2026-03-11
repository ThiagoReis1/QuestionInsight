from numpy import *

vet = array(eval(input()))
cont = 0
j = 0
for i in range(size(vet)):
	if(vet[i]>180.0):
		cont = cont+vet[i]
		j = j+1
if(cont>0):
	print(round(cont/j,2))
else: 
	print("0.0")