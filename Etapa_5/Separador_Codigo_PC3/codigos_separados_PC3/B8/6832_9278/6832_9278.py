produtos = input("Digite a sequencia de produtos (hortifruti=H, cereais=C, laticinios=L): ")

total = 0

for i in range(len(produtos)):
	if produtos[i] == "H":
		total += 5.40
	elif produtos[i] == "C" :
		total += 8.95 
	elif produtos[i] == "L" :
		total += 4.50
		
print(round(total,2))