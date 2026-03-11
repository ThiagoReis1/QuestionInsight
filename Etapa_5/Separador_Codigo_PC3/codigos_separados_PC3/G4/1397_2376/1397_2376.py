#importar modulo maath
from math import*

#Valor da area em hectares
a = float(input("Insira o valor da area: "))

#Condiciona para o calculo do custa
if (a <= 10000):
	c = 5 * a
else:
	c = 50000 + 4 * (a % 10000)
	
print(round(c, 2))
