# faça seu código aqui!
pacote = float(input("quilos: "))
preco = 10.00
#taxas adicionais
if pacote < 5:
	taxa = 3.75
	
elif pacote == 5:
	taxa = 4.75
	
elif pacote > 5:
	taxa = 5.75
	
	
valor_total = preco + taxa
print(round(valor_total,2))
