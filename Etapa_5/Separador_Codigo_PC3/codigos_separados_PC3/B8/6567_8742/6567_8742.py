# faça seu código aqui!
velocidade = int(input("velocidade: "))
if velocidade < 50:
	taxa = 4.50
	valor = 60 + taxa
	print("total=", valor)
elif velocidade == 50:
	taxa = 5.50
	valor = 60 + taxa
	print("total=", valor)
elif velocidade > 50:
	taxa = 6.50
	valor = 60 + taxa
	print("total=", valor)