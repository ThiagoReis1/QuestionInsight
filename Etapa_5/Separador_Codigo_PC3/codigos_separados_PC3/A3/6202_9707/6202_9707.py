altura_bia = 1.69
taxa_bia = 0.01

taxa_crescimento_bia = 0.01


altura_pessoa = float(input())
taxa_pessoa = float(input())

anos = 0

while altura_pessoa <= altura_bia:
	
	 altura_bia += taxa_bia
	 altura_pessoa += taxa_pessoa
	 anos += 1
		
		
print(anos)