altura_luna = 1.65
taxa_luna = 0.02

alt = float(input("Informe sua altura: "))
tx = float(input("Informe sua taxa de crescimento: "))
cont = 0

while(alt < altura_luna):
	alt = alt + tx
	altura_luna = altura_luna + taxa_luna
	
	cont = cont + 1
		
print(cont)