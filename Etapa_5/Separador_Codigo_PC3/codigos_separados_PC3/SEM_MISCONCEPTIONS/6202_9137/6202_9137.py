altura_bia = 1.69
taxa_bia = 0.01

altura_pessoa = float(input())
taxa_pessoa = float(input())

ano = 0

while altura_bia >= altura_pessoa:
	altura_pessoa += taxa_pessoa
	altura_bia += taxa_bia
	ano += 1
	
print(ano)