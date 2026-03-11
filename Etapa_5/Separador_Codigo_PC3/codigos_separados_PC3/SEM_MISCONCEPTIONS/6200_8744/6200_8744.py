altura_cicero = 1.75
taxa_cicero = 0.01
ap = float(input("digite a altura da pessoa: "))
taxa = float(input("digite a taxa: "))

cont = 0

while (ap < altura_cicero):
	altura_cicero = altura_cicero + taxa_cicero
	ap = ap + taxa
	cont = cont + 1
print(cont)
	