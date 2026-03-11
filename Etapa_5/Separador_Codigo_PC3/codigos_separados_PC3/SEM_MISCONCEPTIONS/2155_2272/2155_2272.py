from numpy import*
from math import*
peso=array(eval(input("p:")))
altura=array(eval(input("h:")))
cont=zeros(3,dtype=float)

for x in range(size(peso)):
	imc=peso[x]/(altura[x]**2)
   if(imc<17):
		cont[0]=cont[0]+1
		p="muito abaixo do peso"
	elif(imc<=17 and >= 18.49):
		cont[1]= cont[1] +1 
		p="abaixo do peso"
	elif(imc<=18.5 and >= 24.99):
		cont[2]= cont[2] +1 
		p="peso normal"
	elif(imc<=25 and >= 29.99):
		cont[3]= cont[3] +1 
		p="acima do peso"	
	elif(imc<=30 and >= 34.):
		cont[3]= cont[3] +1 
		p="acima do peso"	
print(round(l,4))
sim=(1/(1+l))
print(round(sim,2))