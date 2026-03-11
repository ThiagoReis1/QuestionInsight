# faça seu código aqui!

tipo = input()
quantidade = int(input())
valor = (quantidade * 25.90) - quantidade * 25.90 * 10 / 100

if tipo.upper() == "B":
	print(round(valor, 2))
else:
	print(round((quantidade * 25.90), 2))

	
