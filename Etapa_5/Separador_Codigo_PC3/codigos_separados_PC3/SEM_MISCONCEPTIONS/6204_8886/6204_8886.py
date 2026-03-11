altura_coelho=float(input("Digite a altura do coelho"))
taxa_coelho= float(input("Digite a taxa de crescimento"))
altura_macaco = 1.86
taxa_macaco = 0.01

cont=0

while altura_coelho <= altura_macaco:
	altura_coelho = altura_coelho + taxa_coelho
	cont = cont + 1
	
	altura_macaco = altura_macaco + taxa_macaco
	
print(cont)
