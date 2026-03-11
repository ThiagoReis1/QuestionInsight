from numpy import*
entrada = input().split(',')
pontos = [0,0,0,0]
jogadores = ['A','B','C','D']

for cesta in entrada:
	if cesta in jogadores:
		pontos[jogadores.index(cesta)] += 1
print(array(pontos))