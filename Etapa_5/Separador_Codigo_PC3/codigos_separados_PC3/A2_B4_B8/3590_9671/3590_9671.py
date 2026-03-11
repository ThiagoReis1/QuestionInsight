from numpy import *

vet = array(eval(input("insira a sequencia das faces acertadas: ")))

i = 0
pontos = 0

while i < size(vet):
	if vet[i] == 1:
		pontos = pontos + 10
		i = i + 1
		
	elif vet[i] == 2:
		pontos = pontos + 5
		i = i + 1
		
	elif vet[i] == 3:
		pontos = pontos
		i = i + 1
		
	elif vet[i] == 4:
		pontos = pontos + 5
		i = i + 1
		
	elif vet[i] == 5:
		pontos = pontos + 20
		i = i + 1
		
	elif vet[i] == 6:
		pontos = pontos + 10
		i = i + 1
	
	total = sum(pontos)

print(total)