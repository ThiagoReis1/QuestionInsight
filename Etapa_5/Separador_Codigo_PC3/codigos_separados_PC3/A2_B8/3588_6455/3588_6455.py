from numpy import *

vet = array(eval(input("Digite os aneis: ")))

i = 0
pontos = 10000

while(i < size(vet)):
	if(vet[i] == 1):
		pontos = pontos * 2
	elif(vet[i] == 2):
		pontos = pontos
	elif(vet[i] == 3):
		pontos = pontos / 2
	elif(vet[i] == 4):
		pontos = pontos / 4
	i = i + 1
	
print(round(pontos, 2))