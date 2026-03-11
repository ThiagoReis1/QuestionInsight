passagem = int(input("qual eh o numero da sua passagem?" ))

if passagem == 175:
	ganhador = "voo premiado"
	print(ganhador)
elif passagem <= 175:
	perdedor_menor = "eh menor"
	print(perdedor_menor)
else:
	perdedor_maior = "eh maior"
	print(perdedor_maior)
# faça seu código aqui!