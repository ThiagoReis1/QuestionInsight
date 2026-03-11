nome = input("Digite o nome: ")
danos = int(input("Valor dos dados: "))
pontos = int(input("Valor dos pontos "))
if (1 <= pontos <= 10):
	if (nome == "AAMUEL") and (2 < danos < 20):
		perda = 8 + 2*((2*pontos)%10)
		print(perda)
	elif (nome == "HETHRADIAH"):
		perda = 2*pontos
		print(perda)
	elif (nome == "RAKSHASA") and (2 < danos < 20):
		perda = 10 + 2*(pontos)%10
		print(perda)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
