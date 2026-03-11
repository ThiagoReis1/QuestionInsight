altura_max = 1.75
taxa_max = 0.01
altura = float(input("digite a altura: "))
taxa = float(input("digite a taxa: "))
anos = 0
while (altura<altura_max):
	altura = altura + taxa
	altura_max = altura_max + taxa_max
	anos= anos +1
print(anos)