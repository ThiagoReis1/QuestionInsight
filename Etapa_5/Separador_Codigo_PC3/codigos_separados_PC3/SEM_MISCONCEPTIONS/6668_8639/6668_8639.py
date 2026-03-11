from numpy import *
valor= array(eval(input("")))

soma=0
cont=0

for i in  valor:
	if i > 170:
		soma += i
		cont += 1

		
if cont > 0:
	media = soma / cont
	print(round(media,2))
	
else:
	print(0.0)

		

