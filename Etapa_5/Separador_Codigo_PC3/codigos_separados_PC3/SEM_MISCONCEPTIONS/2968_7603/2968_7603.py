

item = input("lanche ou salgado: ").upper()
qtd = int(input("qtd de lanche: "))
refri = int(input("qtd de refri: "))

if item == "L":
	saida = ( qtd * 5 ) + ( refri * 4)
	
else:
	saida = ( qtd * 3.5 ) + ( refri * 4)
	
print(round(saida, 2))