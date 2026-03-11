altura_coelho = float(input("insira a altura do coelho:"))
taxa_coelho = float(input("insira o crescimento atual do coelho: "))
altura_macaco = 1.86
taxa_macaco = 0.01

i= 0

while altura_coelho < altura_macaco:
	altura_coelho = altura_coelho + taxa_coelho
	altura_macaco = altura_macaco + taxa_macaco
	i += 1

print(i)
	