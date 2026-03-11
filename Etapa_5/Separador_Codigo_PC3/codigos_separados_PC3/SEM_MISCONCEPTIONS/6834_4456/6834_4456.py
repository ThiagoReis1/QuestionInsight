preco_compra = 0

compra = input()

i = 0

while i < len(compra):
	if(compra[i] == 'C'):
		preco_compra += 10.5
	elif(compra[i] == 'E'):
		preco_compra += 8.75
	else:
		preco_compra += 17.9
	i = i+1
		
print(round(preco_compra,2))

