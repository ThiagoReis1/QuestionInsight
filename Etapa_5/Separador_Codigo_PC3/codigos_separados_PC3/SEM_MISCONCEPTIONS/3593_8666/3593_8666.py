def calcular_pontuacao(face,pontuacao):
	if face == 1 or face == 3 or face == 5:
		return pontuacao / 2
	elif face == 2 or face == 4 or face == 6:
		return pontuacao * 3
	else:
		return pontuacao
	
pontuacao = 200

entrada = input("Digite a sequencia de faces do dado: ")
dado = [int(x) for x in entrada.split(',')]

for dado in dado:
	pontuacao = calcular_pontuacao(dado , pontuacao)
	
print(round(pontuacao_arredondada , 2))