from numpy import *
v=array(eval(input()))
vet=array(eval(input()))
i=0
s=0

while(i<size(vet)):
	if(vet[i]=="QUENTE"):
		s=s+v[i]*90*0.005
	elif(vet[i]=="MORNO"):
		s=s+v[i]*45*0.005
	elif(vet[i]=="FRIO"):
		s=s+v[i]*0*0.005
	
	i=i+1
	
print(round(s,2))



