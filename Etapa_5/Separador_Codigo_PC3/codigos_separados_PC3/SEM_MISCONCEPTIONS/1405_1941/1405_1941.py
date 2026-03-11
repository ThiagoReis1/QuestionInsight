nome_do_ataque = input("digite o nome: ")
dado1 = int(input("digite o valor do dado: "))
dado2 = int(input("digite o valor do dado: "))
if (nome_do_ataque == "grito"):
	pontos_perdidos = 6 + dado1 + dado2
else:
	pontos_perdidos = (dado1 + dado2)**2
print(pontos_perdidos)