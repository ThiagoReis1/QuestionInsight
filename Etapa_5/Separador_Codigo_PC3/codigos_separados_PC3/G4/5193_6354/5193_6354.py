a = float(input("Digite a quantidade de ramem: "))
b = float(input("Digite a quantidade de menma: "))
c = float(input("Digite a quantidade de bolinho de arroz: "))
d = float(input("Digite a quantidade de onigi: "))
					 
	
valor = a * 7.00 + b * 6.00 + c * 3.00 + d * 5.00	

if(valor <= 42.00):
	valor = valor - 3.00
else:
	valor = valor - valor * 0.1
	
print(round(valor, 2), "ryous")