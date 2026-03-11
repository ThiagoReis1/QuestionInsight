altura_luna = 1.65
taxa_luna = 0.02

altura_colega = float(input("Insira a altura do colega: "))
taxa_colega = float(input("Insira a taxa de crescimento do colega: "))

ano = 0

while altura_luna >= altura_colega:
	
	altura_colega += taxa_colega
	altura_luna += taxa_luna
	ano += 1
		
print(ano)