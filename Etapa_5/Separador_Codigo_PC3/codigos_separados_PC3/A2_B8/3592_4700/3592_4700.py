from numpy import*

faces = array(eval(input("Faces do dado tiradas pelo jogador: ")))
pontuacao = 100

for i in faces:
	if (i == 1):
		pontuacao = pontuacao
	elif (i == 2):
		pontuacao = pontuacao*2
	elif (i == 3):
		pontuacao = pontuacao/3
	elif (i  == 4):
		pontuacao = pontuacao*4
	elif (i == 5):
		pontuacao = pontuacao/5
	elif (i == 6):
		pontuacao = pontuacao*6

print(round(pontuacao,2))