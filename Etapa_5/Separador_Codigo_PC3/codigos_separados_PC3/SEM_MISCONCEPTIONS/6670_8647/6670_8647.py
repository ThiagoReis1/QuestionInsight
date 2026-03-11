from numpy import *

valores = array(eval(input("Quais os valores?: ")))

contagem = 0
cont = 0

for i in range(size(valores)):
	if valores[i] > 20:
		contagem += valores[i]
		cont += 1
	
if cont == 0:
	contagem = 0
else:
	contagem = contagem / cont
	
	
print(round(contagem, 2))
		