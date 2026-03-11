altura_max = 1.75
taxa_max = 0.01
cont = 0

altura = float(input("informe a altura: "))
crescimento = float(input("informe seu crescimento: "))

while altura_max > altura:
	altura = altura + crescimento
	altura_max = altura_max + taxa_max
	cont = cont + 1
	
print(cont)