from numpy import*

faces = array(eval(input("numero de faces: ")))
pontos = 200
i = 0

while i < size(faces):
	if faces[i] == 1:
		pontos = pontos /2
	elif faces[i] == 2:
		pontos = pontos * 3
	elif faces[i] == 3:
		pontos = pontos / 2
	elif faces[i] == 4:
		pontos = pontos * 3
	elif faces[i] == 5:
		pontos = pontos / 2
	elif faces[i] == 6:
		pontos = pontos * 3
	i = i + 1
print(round(pontos, 2))