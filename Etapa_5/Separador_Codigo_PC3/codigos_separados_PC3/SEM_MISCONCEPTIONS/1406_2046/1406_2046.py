ataque = input("digite o ataque: ")
valor_dado = int(input("valor do dado: "))
num_turnos = int(input("digite valor de turnos: "))
if (ataque == 'cuspe'):
	pontos = 2 * valor_dado * num_turnos
	print(pontos)
else:
	pontos_2 = valor_dado * num_turnos
	print(pontos_2)