from numpy import *

custo = array(eval(input("Vetor de custo: ")))

cont = 0
custo_total = 0
soma = 0 
desconto = 0

while(cont < size(custo)):
	if(custo[cont] > 80):
		desconto = desconto + 5
	cont = cont + 1
custo_total = sum(custo) - desconto
print(round(custo_total, 2))