altura_joe = 1.77
taxa_joe = 0.02

cont = 0

altura = float(input())
taxa = float(input())



while altura < altura_joe: 
	altura = altura + taxa
	altura_joe = altura_joe + taxa_joe
	
	cont += 1
	
print(cont)
	