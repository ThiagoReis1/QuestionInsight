altura_luna = 1.65
taxa_luna = 0.02

pessoa = float(input("Digite altura: "))
crescimento = float(input("Digite altura: "))

anos = 0

while(pessoa <= altura_luna):
	pessoa += crescimento
	altura_luna += taxa_luna
	anos += 1
	
print(anos)