cabeca = input("nome da cabeça:")
D1 = int(input("valor do dado 1:"))
D2 = int(input("valor do dado 2:"))
D3 = int(input("valor do dado 3:"))

if (cabeca == "Aameul"):
	dano = 8 + (D1 + D2 + D3)
	print(dano)
else:
	dano = 2 * (D1 + D2 + D3)
	print(dano)