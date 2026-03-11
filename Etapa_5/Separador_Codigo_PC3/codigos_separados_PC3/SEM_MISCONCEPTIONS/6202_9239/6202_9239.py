altura_bia = 1.69
taxa_bia = 0.01

pessoa = float(input("altura pessoa: "))
taxa_pessoa = float(input("taxa pessoa: "))
ano = 0

while (pessoa <= altura_bia):
	pessoa += taxa_pessoa
	altura_bia += taxa_bia
	ano += 1
	
print(ano)