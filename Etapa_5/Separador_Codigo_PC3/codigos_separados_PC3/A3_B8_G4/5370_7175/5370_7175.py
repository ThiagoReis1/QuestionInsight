from numpy import *
vet=array(eval(input("numeros:  ")))
i=0
j=1
resp=1

while(j<size(vet)):
	if(vet[j]>=vet[i]):
		resp=0
	elif(vet[j]<vet[i]):
		j=size(vet)
		resp=1
	i=i+1
	j=j+1

	
if(resp==1):
	print("False")
elif(resp==0):
	print("True")
	