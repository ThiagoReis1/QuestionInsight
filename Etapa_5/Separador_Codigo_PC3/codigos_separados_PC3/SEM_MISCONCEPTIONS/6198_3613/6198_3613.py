altura_luna = 1.65
taxa_luna = 0.02

altura_pessoa = float(input())
taxa_pessoa = float(input())
anos = 0

while altura_pessoa < altura_luna:
	altura_pessoa = altura_pessoa +taxa_pessoa
	altura_luna = altura_luna + taxa_luna
	anos+=1
	
print(anos)