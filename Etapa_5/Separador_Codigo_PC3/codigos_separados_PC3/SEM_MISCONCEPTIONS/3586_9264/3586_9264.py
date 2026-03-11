from numpy import *
aneis = array(eval(input("Digite o anel acertado: ")))
pontuacao = 0

for i in range(size(aneis)):
	anel = aneis[i]
	
	if anel == 1:
		pontuacao += 100
	elif anel == 2:
		pontuacao += 60
	elif anel == 3:
		pontuacao += 20
	else:
		pontuacao += 0

print(pontuacao)