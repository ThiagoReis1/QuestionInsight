altura_bia = 1.69
taxa_bia = 0.01

alt = float(input("Altura: "))
tax = float(input("Taxa: "))
cont = 0
while altura_bia>alt:
	alt = alt+tax
	altura_bia = altura_bia+taxa_bia
	cont += 1
	
print(cont)

	