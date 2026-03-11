altura = float(input("digite a altura: "))
taxa = float(input("digite a taxa de crescimento: "))
altura_luna = 1.65
taxa_luna = 0.02
anos = 0

while (altura < altura_luna):
	altura = altura + taxa
	altura_luna = altura_luna + taxa_luna
	anos = anos + 1
print(anos)
