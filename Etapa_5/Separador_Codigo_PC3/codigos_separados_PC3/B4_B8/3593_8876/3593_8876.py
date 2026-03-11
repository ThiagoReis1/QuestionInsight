from numpy import *

face = array(eval(input("Face: ")))
pontos = 200

i = 0

while i < size(face):
	if face[i] == 1: 
		pontos = pontos / 2
	elif face[i] == 2:
		pontos = pontos * 3 
	elif face[i] == 3:
		pontos = pontos / 2
	elif face[i] == 4:
		pontos = pontos * 3
	elif face[i] == 5:
		pontos = pontos / 2
	elif face[i] == 6:
		pontos = pontos * 3
	i = i + 1

print(round(pontos, 2))
