#Universidade Federal do Amazonas - UFAM ; Laís Amorim - 21602327
from numpy import *
temperaturas = eval(input("Informe o vetor: "))
valores_validos = 0 
i = 0
while(i < size(temperaturas)):
	if(temperaturas[i] > -100):
		valores_validos = valores_validos + 1
	i = i + 1
vetor_novo = array(zeros(valores_validos, dtype = float))
i = 0 
j = 0
while(i<size(temperaturas)):
	if(temperaturas[i] > -100):
		vetor_novo[j] = temperaturas[i]
		j = j+1
	i = i+1
print(vetor_novo)

