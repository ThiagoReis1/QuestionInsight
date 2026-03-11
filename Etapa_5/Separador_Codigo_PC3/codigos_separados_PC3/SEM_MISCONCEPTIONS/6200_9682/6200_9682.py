altura_max = 1.75
taxa_max = 0.01
altura = float(input("Digite a sua altura: "))
taxa = float(input("Digite a sua taxa de crescimento: "))
anos = 0
while altura < altura_max:
	altura += taxa
	altura_max += taxa_max
	anos += 1
	
print(anos)