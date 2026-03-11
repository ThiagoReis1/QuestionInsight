altura = float(input("ALTURA: "))
tx = float(input(""))

cont = 0

altura_bia = 1.69
taxa_bia = 0.01

while altura_bia > altura:
	altura_bia = altura_bia + taxa_bia
	altura = altura + tx
	cont = cont + 1
print(cont)
