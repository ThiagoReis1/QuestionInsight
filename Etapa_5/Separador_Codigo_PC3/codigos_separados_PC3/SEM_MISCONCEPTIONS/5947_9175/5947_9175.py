item = input("Digite 'C' para coxinha e 'E' para esfirra: ")
quantidades = int(input("Digite a quantidade de coxinhas ou esfirras: "))
quantidade_de_sucos = int(input("Digite a quantidade de sucos: "))

coxinha = 2.00
esfirra = 4.50
suco = 6.00

if item == 'C':
	valor_total_compra = quantidades * coxinha + quantidade_de_sucos * suco
	print(round(valor_total_compra, 2))
	
else: 
	valor_total_compra = quantidades * esfirra + quantidade_de_sucos * suco
	print(round(valor_total_compra, 2))
	
	
	
	
	



