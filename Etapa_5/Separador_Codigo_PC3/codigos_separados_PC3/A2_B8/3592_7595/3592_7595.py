from numpy import *
numeros = array(eval(input("Faces do dado: ")))

pontuacao = 100

i = 0

while(i < size(numeros)):
	if(numeros[i] == 1):
		pontuacao = pontuacao
	elif(numeros[i] == 2):
		pontuacao = pontuacao *2
	elif(numeros[i] == 3):
		pontuacao = pontuacao / 3
	elif(numeros[i] == 4):
		pontuacao = pontuacao * 4
	elif(numeros[i] == 5):
		pontuacao = pontuacao /5
	elif(numeros[i] == 6):
		pontuacao = pontuacao *6
	i = i + 1	
print(round(pontuacao,2))