# faça seu código aqui!
combo = input("combo desejado:")
quantidade = int(input("Quantidade de combos:"))
if (combo.upper() == "C"):
	valor = (quantidade * 30) 
	desconto = valor - (valor * (15/100))
	print(round(desconto, 2))

else:
	valor = quantidade * 30
	print(valor)
	