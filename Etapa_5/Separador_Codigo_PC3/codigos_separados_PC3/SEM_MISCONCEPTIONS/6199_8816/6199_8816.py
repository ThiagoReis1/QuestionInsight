altura_cicero = 1.8
taxa_cicero = 0.01

altura_2 = float(input("Sua altura: "))
taxa_2 = float(input("Sua taxa de crescimento: "))
cont = 0
while altura_2 <= altura_cicero:
	cont = cont + 1
	altura_cicero = altura_cicero + taxa_cicero
	altura_2 = altura_2 + taxa_2
	
print(cont)