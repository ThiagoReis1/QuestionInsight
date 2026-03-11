#Entrada de dados 

peso_da_encomenda =  float(input("Qual o peso da encomenda? "))

if(peso_da_encomenda <  4999.9):
	print(round(0.05 * peso_da_encomenda,2))

else:
	print(round(0.04 * peso_da_encomenda + 60.00, 2))


