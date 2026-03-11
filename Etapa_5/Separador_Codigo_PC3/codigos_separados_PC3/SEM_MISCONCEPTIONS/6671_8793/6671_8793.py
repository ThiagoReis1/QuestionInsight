from numpy import *

me = array(eval(input("Insira os valores dos vetores: ")))

soma = 0 
contador = 0

for i in me:
	if i > 15:
		soma += i
		contador += 1
if contador > 0:
	media = round(soma/contador,2)
	print(media)
else:
	print(0.0)




