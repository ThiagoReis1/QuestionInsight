altura_bia = 1.69
taxa_bia = 0.01
altura = float(input("Informe a altura: "))
taxa = float(input("Informe a taxa: "))
cont = 0

while altura<altura_bia:
	altura_bia = altura_bia+taxa_bia
	altura = altura+taxa
	cont = cont+1
	
print(cont)