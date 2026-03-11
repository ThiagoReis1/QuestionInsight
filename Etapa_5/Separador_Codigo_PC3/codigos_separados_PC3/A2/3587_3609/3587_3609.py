from numpy import *

pontuacao = 100
vetor = eval(input())

for i in vetor:
	if(i== 1):
		pontuacao *=5
	elif(i == 2):
		pontuacao *=3
	elif(i == 3):
		pontuacao = pontuacao
	else:
		pontuacao /=2
print(round(pontuacao,2))