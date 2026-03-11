compra= input("digite a sequencia de produtos (Adega=A, Laticinios=L, Padaria=P): ")

preco_total= 0

for i in range(len(compra)):
	if compra[i] == 'A':
		preco_total += 16.75
	elif compra[i] == 'L':
		preco_total += 4.60
	elif compra[i] == 'P':
		preco_total += 2.85
	
preco_total = round(preco_total, 2)
print(preco_total)
