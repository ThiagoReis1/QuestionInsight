compra = input("Digite a sequencia de produtos (Biscoitos=B,Cereais=C, Enlatado=E): ")
preco_total = 0

for i in range(len(compra)):
	if compra [i] == 'B':
		preco_total +=3.75
	elif compra[i] == 'C':
		preco_total +=7.90
	elif compra[i] == 'E':
		preco_total +=9.85
preco_total = round(preco_total,2)
print(preco_total)
