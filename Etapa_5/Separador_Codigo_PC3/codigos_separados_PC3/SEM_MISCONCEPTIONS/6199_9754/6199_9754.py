altura = float(input("Digite um altura: "))
taxa = float(input("Digite a taxa: "))
contador = 0

Altura_cicero = 1.8
taxa_cicero = 0.01

while altura < Altura_cicero:
	altura = altura + taxa
	Altura_cicero = Altura_cicero + taxa_cicero
	contador = 	contador + 1
print(contador)
	
	