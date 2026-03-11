# faça seu código aqui!
lvg = 30.0
qtd = int(input("insira a quantidade de roupas para lavagem:"))

if qtd < 10:
	taxa = lvg +3.25
	print(taxa)
elif qtd == 10:
	taxa = lvg + 4.50
	print(taxa)
else:
	taxa = lvg + 6.00
	print(taxa)