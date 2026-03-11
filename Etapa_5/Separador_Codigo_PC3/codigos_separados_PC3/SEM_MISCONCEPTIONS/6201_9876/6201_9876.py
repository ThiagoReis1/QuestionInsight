altura_joe = 1.77
taxa_joe = 0.02

alt = float(input("insira a altura: "))
taxa = float(input("insira a taxa: "))

anos = 0

while alt < altura_joe:
	altura_joe += taxa_joe
	alt += taxa
	anos += 1 
print(anos)
		
	
