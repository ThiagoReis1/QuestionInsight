ataque = input("tipo de ataque realizado pelo Cornugon: ")
valor = int(input("valor sorteado no lancamento do dado: "))
turnos = int(input("numero de turnos que o personagem fica ferido: "))
if (ataque == "cuspe"):
	pontos = 2*valor*turnos
	print(pontos)
else:
	print(valor*turnos)