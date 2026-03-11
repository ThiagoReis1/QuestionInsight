numero_aboboras = int(input("digite a quantidade: "))

valor_aboboras1 = 3.80
valor_aboboras2 = 3.45

if(numero_aboboras >=5):
	compra = (numero_aboboras * valor_aboboras2)
	
else:
	compra = (numero_aboboras * valor_aboboras1)
	
print(round(compra, 2))