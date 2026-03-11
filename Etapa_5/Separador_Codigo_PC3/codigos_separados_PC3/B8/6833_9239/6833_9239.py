produtos = input("produtos M,P e R: ")
preco_total = 0 

for y in range(len(produtos)):
	if produtos[y] == 'M':
		preco_total += 7.25
	elif produtos[y] == 'P':
		preco_total += 4.75
	elif produtos[y] == 'R':
		preco_total += 3.50
		
preco_total = round(preco_total, 2)
print(preco_total)
