from numpy import *

face = array(eval(input('insira a pontuacao total: ')))

i = 0
pontos = 0
while i < size(face):
	if face[i] == 1:
		pontos += 10
	elif face[i] == 2:
		pontos += 5
	elif face[i] == 4:
		pontos += 5
	elif face[i] == 5:
		pontos += 20
	elif face[i] == 6:
		pontos += 10
	i += 1
		
print(round(pontos))