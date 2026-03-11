altura_bia = 1.69
taxa_bia = 0.01

a = float(input("Altura da pessoa: "))
b = float(input("Taxa de Crescimento da pessoa: "))
anos = 0

while a <= altura_bia:
	a = a+b
	altura_bia = altura_bia+taxa_bia
	anos += 1

print(anos)