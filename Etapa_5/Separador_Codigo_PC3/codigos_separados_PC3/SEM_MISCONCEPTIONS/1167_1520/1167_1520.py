# -------------------------------------------------------
#Everaldo Oliveira Silva - matricula 21453644

from math import*

N = int(input("digite o valor do termo: "))
i = 1
total = (1 ** 2) / 0
total = (-1 ** 2) / 0
x = 0
while (1 != N )
	if(N % 2 != 0)
		i = 1 + 1
		total = total + (1 ** 2) / (x + 2)
	else:
		i = 1 + 1
		total = total - (1 ** 2) / (x + 2)
		
print(round(total, 11))
