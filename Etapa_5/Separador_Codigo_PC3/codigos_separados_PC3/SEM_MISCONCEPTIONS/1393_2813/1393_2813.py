peso = float(input("peso da encomenda: "))
gramas = 4999.9
if(peso < gramas):
	conta1 = peso*0.05
	print(round(conta1,2))

else:
	conta2 = (peso*0.04) + 60
	print(round(conta2, 2))