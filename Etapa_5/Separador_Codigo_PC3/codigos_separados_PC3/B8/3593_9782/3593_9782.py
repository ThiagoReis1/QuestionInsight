from numpy import *

dados = array(eval(input("Quais foram os valores: ")))

i = 0
pontuacao = 200.

while i < size(dados):
	if dados[i] == 1 or dados[i] == 3 or dados[i] == 5:
		pontuacao /= 2
	elif dados[i] == 2 or dados[i] == 4 or dados[i] == 6:
		pontuacao *= 3
	i += 1
print(round(pontuacao, 2))
	