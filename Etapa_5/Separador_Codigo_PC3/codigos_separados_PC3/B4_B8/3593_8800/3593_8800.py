from numpy import*

faces = array(eval(input("digite os valores das faces: ")))

i = 0

pontuacao = 200

while i < size(faces):
	if faces[i] == 1:
		pontuacao = pontuacao / 2
	elif faces[i] == 2:
		pontuacao = pontuacao * 3
	elif faces[i] == 3:
		pontuacao = pontuacao / 2
	elif faces[i] == 4:
		pontuacao = pontuacao * 3
	elif faces[i] == 5:
		pontuacao = pontuacao / 2
	elif faces[i] == 6:
		pontuacao = pontuacao * 3
	i = i + 1
print(round(pontuacao, 2))