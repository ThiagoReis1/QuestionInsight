comida = input("Fatia de torta ou pastel: ")

qtd_comida = int(input("Quantidade de itens de comida: "))
qtd_bebida = int(input("Quantidade de bebidas: "))

torta = 6.00
pastel = 5.00
capuccino = 4.50

if comida.upper() == "P":
	valor = (qtd_comida * pastel) + (qtd_bebida * capuccino)
else: 
	valor = (qtd_comida * torta) + (qtd_bebida * capuccino)

print(round(valor,1))
	
	