altura_bia = 1.69
taxa_bia = 0.01
anos = 0
altura_pessoa = float(input())
taxa_pessoa = float(input())

while(altura_pessoa < altura_bia):
	altura_bia += taxa_bia
	altura_pessoa += taxa_pessoa
	anos+=1
print(anos)