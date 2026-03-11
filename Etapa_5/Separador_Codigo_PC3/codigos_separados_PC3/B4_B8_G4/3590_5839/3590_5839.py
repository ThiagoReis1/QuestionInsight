from numpy import * 

face = array(eval(input("Digite as faces tiradas: ")))
x = size(face)

i = 0
pontos = 0

while (i < x):
	if (face[i] == 1):
		pontos = pontos + 10
		i = i + 1
	elif (face[i] == 2):
		pontos = pontos + 5
		i = i + 1
	elif (face[i] == 3):
		pontos = pontos + 0
		i = i + 1
	elif (face[i] == 4):
		pontos = pontos + 5
		i = i + 1
	elif (face[i] == 5):
		pontos = pontos + 20
		i = i + 1
	elif (face[i] == 6):
		pontos = pontos + 10
		i = i + 1
		
print(pontos)