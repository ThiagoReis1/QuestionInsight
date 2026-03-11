# faça seu código aqui!

qtd = int(input("Quantidade de pecas: "))

if qtd == 10:
	custo = 30 + 4.50
elif qtd < 10:
	custo = 30 + 3.25
else:
	custo = 30 + 6.00
print(round(custo, 2))