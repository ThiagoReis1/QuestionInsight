from numpy import *
vetor=array(eval(input("Vetor de numeros: ")))
ind=0
pontos=100

while ind<size(vetor):
	if vetor[ind]==1:
		pontos=pontos
	if vetor[ind]==2:
		pontos=pontos*2
	if vetor[ind]==3:
		pontos=pontos/3
	if vetor[ind]==4:
		pontos=pontos*4
	if vetor[ind]==5:
		pontos=pontos/5
	if vetor[ind]==6:
		pontos=pontos*6
	ind=ind+1
print(round(pontos,2))


	
