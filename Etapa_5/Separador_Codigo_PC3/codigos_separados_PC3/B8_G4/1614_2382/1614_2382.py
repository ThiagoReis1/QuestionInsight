from numpy import *
vet=array(eval(input()))
v=array(eval(input()))
i=0
s=0

while(i<size(vet)):
	if(vet[i]=="BANANA"):
		s=s+v[i]*0.97
	elif(vet[i]=="BIFE"):
		s=s+v[i]*2.95
	elif(vet[i]=="FEIJOADA"):
		s=s+v[i]*1.27
	elif(vet[i]=="OMELETE"):
		s=s+v[i]*1.04
	elif(vet[i]=="TOMATE"):
		s=s+v[i]*0.2
	
	
	i=i+1
	
print(round(s,2))



