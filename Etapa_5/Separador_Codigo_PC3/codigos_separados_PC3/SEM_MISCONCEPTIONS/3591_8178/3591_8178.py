from numpy import* 

dados = array(eval(input()))
pontuacao = 0
indice = 0
n = len(dados)

while indice < n:
	if dados[indice] in [1, 3, 5]:
		pontuacao += 10
	else:
		pontuacao += 5
	indice += 1
	
print(pontuacao)