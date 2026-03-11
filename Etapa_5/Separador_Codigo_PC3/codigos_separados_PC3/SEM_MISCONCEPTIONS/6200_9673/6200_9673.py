altura = float(input("qual eh a altura: "))
crescimento = float(input("qual a taxa de crescimento: "))

altura_max = 1.75
taxa_max = 0.01
contadora = 0

while (altura < altura_max):
	altura = altura + crescimento
	altura_max = altura_max + taxa_max
	contadora = contadora + 1
print(contadora)