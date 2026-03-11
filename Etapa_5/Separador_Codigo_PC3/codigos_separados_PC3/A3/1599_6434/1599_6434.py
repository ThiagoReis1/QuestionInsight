from numpy import*
vetor_custo = array(eval(input("Insira o vetor: ")))

cont=0
custo_total=0

while(cont < size(vetor_custo)):
	if(vetor_custo[cont] > 80):
		custo_total= vetor_custo[cont] - (vetor_custo[cont]*15)/100
	else:
		custo_total+= vetor_custo[cont]
	
	
	cont=cont+1

print(round(custo_total,2))