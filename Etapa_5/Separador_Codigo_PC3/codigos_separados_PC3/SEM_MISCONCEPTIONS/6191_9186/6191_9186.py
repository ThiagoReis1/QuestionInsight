moeda = input("Digite 'cara' ou 'coroa':")
cont = 0
while moeda != 'S':
	if moeda == "CARA":
		cont += 1
	moeda = input("Digite 'cara' ou 'coroa':")
		
print(cont)