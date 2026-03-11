altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho = float(input('Digite a altura:'))
taxa_coelho = float(input('Digite a taxa de crescimento:'))

anos = 0

while altura_coelho < altura_macaco:
	altura_coelho = altura_coelho + taxa_coelho 
	altura_macaco = altura_macaco + taxa_macaco
	anos = anos + 1
print(anos)
	
	

	