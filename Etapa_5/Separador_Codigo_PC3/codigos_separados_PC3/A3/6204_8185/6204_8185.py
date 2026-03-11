altura_macaco = 1.86
taxa_macaco = 0.01
altura_coelho = float(input("Altura do coelho: "))
taxa_coelho = float(input("Taxa do coelho: "))
cont = 0

while taxa_coelho < taxa_macaco:
	if taxa_coelho > taxa_macaco:
		r = taxa_coelho*altura_coelho*t/100