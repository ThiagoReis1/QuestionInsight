aneis_acertados = input("digite:")

pontuacao = 10000

for anel in aneis_acertados:
	if anel == '1':
		pontuacao *= 2
	elif anel == '3':
		pontuacao /= 2
	elif anel == '4':
		pontuacao /= 4
		
pontuacao_arredondada = round(pontuacao, 2)

print("{:.2f}".format(pontuacao_arredondada))