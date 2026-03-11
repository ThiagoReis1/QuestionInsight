ataque = input("Tipo de ataque:")
rodada = int(input("Numero de rodadas:"))
valor1 = int(input("Valor1 sorteado:"))
valor2 = int(input("Valor2 sorteado:"))
if (ataque == "constricao"):
	pontos_vida = (valor1+valor2+1)*rodada
	print(pontos_vida)
else:
	pontos_vida = valor1*valor2
	print(pontos_vida)
	