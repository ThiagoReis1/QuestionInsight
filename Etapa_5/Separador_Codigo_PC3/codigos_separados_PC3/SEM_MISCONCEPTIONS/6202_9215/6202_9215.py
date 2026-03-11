altura_bia = 1.69
taxa_bia = 0.01


altura_pessoa = float(input("digite a altura da pessoa: "))
taxa_pessoa = float(input("digite a taxa de crescimento: "))

while (altura_bia) < (altura_pessoa):
	altura_bia += taxa_bia
	altura_pessoa += taxa_pessoa
	anos += 0
	
print(anos)
	
	
