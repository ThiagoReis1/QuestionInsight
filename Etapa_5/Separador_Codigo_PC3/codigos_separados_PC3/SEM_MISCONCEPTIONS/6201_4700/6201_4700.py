altura_joe = 1.77
taxa_joe = 0.02

altura = float(input("Digite a altura da pessoa: "))
taxa = float(input("Digite a taxa de crescimento da pessoa: "))
contador = 0

while (altura < altura_joe):
	altura = (altura + taxa)
	altura_joe = (altura_joe + taxa_joe)
	contador += 1
print (contador)