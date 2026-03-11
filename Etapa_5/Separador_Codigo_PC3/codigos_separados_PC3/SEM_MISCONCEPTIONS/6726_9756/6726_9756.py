numerox = int(input("Escreva um numero inteiro para ser o valor de X: "))

quociente = numerox // 29
resto = numerox % 29

if numerox % 29 == 0:
	print (quociente)
	print ("sim")
else:
	print (resto)
	print ("nao")
