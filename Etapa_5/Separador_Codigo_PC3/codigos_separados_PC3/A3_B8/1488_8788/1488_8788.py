from math import*

valor = 0.0 

consumo = float(input('insira o consumo em minutos do cliente:'))


if consumo >= 0 and consumo <= 100:
	valor = consumo * 1.2 + 1
elif consumo > 100 and consumo <= 200:
	valor = consumo * 1.3 + 10
elif consumo > 200 and consumo <= 300:
	valor = consumo * 1.4 + 20
elif consumo > 300:
	valor = consumo * 1.5 + 25
		
print(round(valor,2))
	