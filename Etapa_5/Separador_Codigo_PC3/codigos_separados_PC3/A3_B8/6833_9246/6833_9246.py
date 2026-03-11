produtos = input("digite: ")
total = 0
mercearia = 0
padaria = 0
rotisseria = 0

i = 0 
while i < len(produtos):
	produto = produtos[i]
	if produto == 'M':
		total += 7.25
		mercearia += 1
	elif produto == 'P':
		total += 4.75	
		padaria += 1
	elif produto == 'R':
		total += 3.50
		rotisseria += 1
	i += 1

total = round(total, 2)
print(total)