cenouras = int(input("digite o numero de cenouras: "))

if cenouras < 5:
	valor = cenouras * 1.20
	
else:
	valor = cenouras * 0.90
	
print(round(valor, 2))