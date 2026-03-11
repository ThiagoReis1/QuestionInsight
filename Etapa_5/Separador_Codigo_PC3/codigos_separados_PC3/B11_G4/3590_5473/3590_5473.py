from numpy import *

face = array(eval(input("Informe as faces: ")));
i = 0
soma = 0
while(i<size(face)):
	if(face[i]==1):
		soma = soma + 10
	if(face[i]==2):
		soma = soma + 5
	if(face[i]==3):
		soma = soma + 0
	if(face[i]==4):
		soma = soma + 5
	if(face[i]==5):
		soma = soma + 20
	if(face[i]==6):
		soma = soma + 10
	
	i = i + 1 

print(soma)