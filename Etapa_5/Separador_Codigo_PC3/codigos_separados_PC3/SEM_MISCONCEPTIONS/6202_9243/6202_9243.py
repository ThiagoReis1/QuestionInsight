altura_bia = 1.69
taxa_bia = 0.01

pessoa = float(input("Digite altura: "))
crescimento = float(input("Digite altura: "))


anos = 0 


while(pessoa <= altura_bia):
	pessoa += crescimento
	altura_bia += taxa_bia
	anos += 1
	
print(anos)