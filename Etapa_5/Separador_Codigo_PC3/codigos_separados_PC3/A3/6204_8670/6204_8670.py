altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho = float(input("Informe a altura do coelho: "))
taxa_coelho = float(input("Informe a altura do coelho: "))

anos = 0
while (altura_coelho < altura_macaco):
	altura_macaco = altura_macaco + 0.01
	altura_coelho = altura_coelho + taxa_coelho
	anos = anos + 1
	
print(anos)