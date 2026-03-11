cabeca = input("nome da cabeca de demogorgon: ")
dado1 = int(input("valor do dado 1: "))
dado2 = int(input("valor do dado 2: "))
if (cabeca == "AAMEUL") and (dado1 >= 1) and (dado1 <= 10):
	vida = 8 + (dado1 + dado2)
	print(vida)
elif (cabeca == "HETHRADIAH") and (dado1 >= 1) and (dado1 <= 10):
	vida = 2*(dado1 + dado2)
	print(vida)
elif (cabeca == "RAKSHASA") and (dado1 >= 1) and (dado1 <= 10):
	vida = 10 + (dado1 + dado2)
	print(vida)
else:
	print("Entrada invalida")