cabeca = input("Nome da Cabeça (Aameul ou Hethradiah): ")

dado1 = int(input("Valor dado 1: "))
dado2 = int(input("Valor dado 2: "))
dado3 = int(input("Valor dado 3: "))

if(cabeca == "Aameul"):
	dano = 8 + dado1 + dado2 + dado3

if(cabeca == "Hethradiah"):
	dano = (dado1 + dado2 + dado3) * 2

print(dano)