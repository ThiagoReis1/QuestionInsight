from numpy import *
aneis = eval(input("Digite o vetor de aneis pelo jogador: "))
pontuacao_total = 0 

for i in range (len(aneis)):
	anel = aneis [i]
	if anel == 1:
		pontuacao_total +=80
	elif anel == 2:
		pontuacao_total +=40
	elif anel == 3:
		pontuacao_total +=20
	elif anel == 4:
		pontuacao_total +=10
print(pontuacao_total)
