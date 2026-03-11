altura = float(input("Qual a altura que voce deseja?: "))
crescimento = float(input("Qual a taxa que deseja:?"))

altura_cicero = 1.8
taxa_cicero = 0.01
anos = 0

while (altura < altura_cicero):
	altura = altura + crescimento
	altura_cicero = altura_cicero + taxa_cicero
	anos = anos + 1	

print(anos)