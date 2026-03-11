altura_pessoa = float(input("Qual a altura da pessoa? "))
taxa_crescimento = float(input("Qual a taxa de crescimento? "))
altura_chico = 1.5
taxa_chico = 0.002
cont = 1.5
while altura_pessoa != altura_chico:
	
	x = (altura_chico * taxa_chico) / taxa_crescimento
	y = altura_pessoa * taxa_chico
	
print(cont)