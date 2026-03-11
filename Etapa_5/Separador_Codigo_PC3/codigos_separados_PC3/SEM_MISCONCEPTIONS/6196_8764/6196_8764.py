alt = float(input("Digite sua altura: "))
taxa = float(input("Digite sua taxa de crescimento: "))

altura_chico = 1.5
taxa_chico = 0.02

cont = 0
while (alt < altura_chico):
	altura_chico = altura_chico + taxa_chico
	alt = alt + taxa
	cont = cont + 1
print(cont)

	