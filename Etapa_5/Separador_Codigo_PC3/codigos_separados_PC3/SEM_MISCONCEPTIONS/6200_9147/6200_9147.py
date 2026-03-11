altura_max = 1.75
taxa_max = 0.01

alt =float(input("Digite a Altura: "))
taxa = float(input("Digite a Taxa de crescimento: "))
cont = 0


while	altura_max > alt:
	alt = alt + taxa
	altura_max = altura_max + taxa_max
	cont += 1
	
print(cont)