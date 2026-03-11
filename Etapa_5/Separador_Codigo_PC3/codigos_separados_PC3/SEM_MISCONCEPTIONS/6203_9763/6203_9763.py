altura_macaco = 1.4
taxa_macaco = 0.06

altura = float(input("Informe a altura do leao: "))
tx = float(input("Informe a taxa de crescimento do leao: "))
anos = 0

while altura_macaco < altura:
	altura_macaco = altura_macaco + taxa_macaco
	altura = altura + tx
	anos = anos + 1
	
	
print(anos)