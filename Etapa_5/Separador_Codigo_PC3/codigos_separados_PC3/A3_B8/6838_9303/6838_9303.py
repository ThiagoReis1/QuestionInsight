produtos = input("produtos: ")
total = 0
doces = 0
salgados = 0
integrais = 0

i = 0
while i < len(produtos):
	produto = produtos[i]
	if produto == 'D':
		doces +=1
		total += 2.25
	elif produto == 'S':
		salgados += 1
		total += 4.00
	elif produto == 'I':
		integrais += 1
		total += 6.90
	i += 1

total = round(total,2)
print(total)
