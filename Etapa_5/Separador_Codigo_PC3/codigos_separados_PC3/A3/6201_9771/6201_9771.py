altura_joe = 1.77
taxa_joe = 0.02
contador = 0

altura = float(input())
taxa_crescimento = float(input())

anos = 0

while altura < altura_joe:
	altura += taxa_crescimento
	altura_joe += taxa_joe
	
	anos += 1
	
print(anos)