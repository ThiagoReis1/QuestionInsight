from numpy import *
vnotas = array(eval(input("notas: ")))
i=0
soma=0
somap=0
while(i<size(vnotas)):
	e=vnotas[i]*(i+1)
	soma=soma+e
	somap=somap+(i+1)
	
	i=i+1

n=soma/somap
	
print(round(n,2))