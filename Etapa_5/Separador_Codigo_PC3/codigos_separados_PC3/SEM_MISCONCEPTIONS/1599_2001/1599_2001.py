from numpy import *
from math import *

valores = array(eval(input("Digite os valores da compra: ")))

i = 0

while (i - 1 < size(valores)):
	i = i + 1
	if (valores[i] > 80):
		valores[i] = valores[i] * 0.85
else:
		valores[i] = valores[i]

print(sum(valores))					
										

			
