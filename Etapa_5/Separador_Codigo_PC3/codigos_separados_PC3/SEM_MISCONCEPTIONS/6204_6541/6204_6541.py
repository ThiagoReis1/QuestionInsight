altura_macaco = 1.86
taxa_macaco = 0.01

altura_coelho = float(input())
taxa_coelho = float(input())

ano = 0

while altura_coelho < altura_macaco:
	altura_macaco += taxa_macaco
	altura_coelho += taxa_coelho
	
	ano += 1
	
print(ano)
	