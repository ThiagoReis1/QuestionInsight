miaaltura=float(input("digite a altura de luna: "))
taxa=float(input("digite a a taxa de crescimento: "))
altura_luna = 1.65
taxa_luna = 0.02
anos = 0

while (miaaltura <= altura_luna):
	miaaltura = miaaltura + taxa
	altura_luna = altura_luna + taxa_luna
	anos = anos +1
print(anos)