unidade = input("Digite C ou P: ").upper()
valor = float(input("Digite o valor da medida: "))

C = 0.393701 * valor

P = valor/0.393701 

if unidade == "P":
	
	print(round(P,2))

else:
	
	print(round(C,2))
	
	


