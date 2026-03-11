altura_bia = 1.69
taxa_bia = 0.01
altura = float(input("digite a altura: "))
taxa = float(input("digite a taxa: "))
anos = 0
while (altura<=altura_bia):
	altura = altura + taxa
	altura_bia = altura_bia + taxa_bia
	anos= anos +1
print(anos)