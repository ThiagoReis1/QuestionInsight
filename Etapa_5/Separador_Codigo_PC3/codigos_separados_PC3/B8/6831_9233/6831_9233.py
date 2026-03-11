produto = input("digite a sequencia de produtos (ADEGA=A, LATICINIOS=L, PADARIA=P): ")
total = 0
for i in range(len(produto)):
	if produto[i] == 'A':
		total += 16.75
	elif produto[i] == 'L':
		total += 4.60
	elif produto[i] == 'P':
		total += 2.85

total = round(total, 2)
print(total)