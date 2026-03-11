from numpy import *

faces = array(eval(input('Digite as faces: ')))
pontos = 0

for i in faces:
	if i == 1 or i == 3 or i == 5:
		pontos = pontos + 10
	elif i == 2 or i == 4 or i == 6:
		pontos = pontos + 5
print(pontos)