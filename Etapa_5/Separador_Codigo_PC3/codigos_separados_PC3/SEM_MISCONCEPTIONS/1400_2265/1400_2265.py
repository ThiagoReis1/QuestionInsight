tipo_de_ataque = input("Digite um ataque(cosntricao ou polen):")
numero_de_rodada = float(input("Digite um numero de rodadas nas garras da Vinha:"))
lancamento_do_D1 = float(input("Digite um valor de lance do dado D1 de 1 a 6:"))
lancamento_do_D2 = float(input("Digite um valor de lance do dado D2 de 1 a 6:"))

N = lancamento_do_D1 + lancamento_do_D2 


if(tipo_de_ataque.lower() == "polen"):
	pontos_de_vida = (lancamento_do_D1 * lancamento_do_D2)

else:
	pontos_de_vida = (N + 1 * numero_de_rodada)
	
print(pontos_de_vida)