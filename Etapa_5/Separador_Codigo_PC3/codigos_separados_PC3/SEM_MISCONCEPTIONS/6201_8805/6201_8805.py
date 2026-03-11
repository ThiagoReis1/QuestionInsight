altura_joe = 1.77
taxa_joe = 0.02

altura_x = float(input("Altura: "))
crescimento_x = float(input("Crescimento: "))

anos = 0

while (altura_x < altura_joe):
	altura_joe += taxa_joe
	altura_x += crescimento_x
	anos += 1
print(anos)	
	
	