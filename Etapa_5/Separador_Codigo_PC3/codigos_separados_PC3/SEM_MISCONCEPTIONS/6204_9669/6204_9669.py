altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho = float(input("Entre com a altura do coelho: "))
taxa_coelho = float(input("Entre com a taxa de crescimento do coelho: "))

ano = 0
while altura_coelho <= altura_macaco:
	if taxa_coelho > taxa_macaco:
		ano = ano + 1
		altura_coelho = altura_coelho + taxa_coelho
		altura_macaco = altura_macaco + taxa_macaco
	
print(ano)
		
		