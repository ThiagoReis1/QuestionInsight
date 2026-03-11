altura = float(input("Digite a altura: "))
taxa = float(input("Digite a taxa: "))

altura_chico = 1.5
taxa_chico = 0.02
cont = 0

while altura_chico > altura:
	altura_chico = altura_chico + taxa_chico
	altura = altura + taxa
	cont = cont + 1
print(cont)
	