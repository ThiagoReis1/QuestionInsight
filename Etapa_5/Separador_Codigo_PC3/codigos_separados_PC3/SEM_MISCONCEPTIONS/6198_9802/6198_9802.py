altura_luna = 1.65
taxa_luna = 0.02

altura = float(input("insira a altura: "))
taxa = float(input("insira a taxa: "))

anos = 0

while altura <= altura_luna:
	altura_luna = altura_luna + taxa_luna
	altura = altura + taxa
	anos = anos + 1
print(anos)