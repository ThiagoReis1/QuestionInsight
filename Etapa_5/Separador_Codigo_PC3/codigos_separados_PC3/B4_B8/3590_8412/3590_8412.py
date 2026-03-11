from numpy import *
vet = array(eval(input("insira o vetor: ")))
pontuacao = 0

for i in range(size(vet)):
	if vet[i] == 1:
		pontuacao = pontuacao + 10
	elif vet[i] == 2:
		pontuacao = pontuacao + 5
	elif vet[i] == 4:
		pontuacao = pontuacao + 5
	elif vet[i] == 5:
		pontuacao = pontuacao + 20
	elif vet[i] == 6:
			pontuacao = pontuacao + 10
print(pontuacao)
