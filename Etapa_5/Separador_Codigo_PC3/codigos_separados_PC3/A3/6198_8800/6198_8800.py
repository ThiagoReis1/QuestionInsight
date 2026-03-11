altura_luna = 1.65
taxa_luna = 0.02
altura = float(input("digite a altura"))
taxa = float(input("digite a taxa de crescimento"))
cont = 0

while altura_luna > altura:
	cont = cont + (taxa + altura)
print(cont)
	