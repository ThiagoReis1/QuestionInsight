from math import*
#Entradas
x = float(input("Digite o valor de x: ")) #O valor de x

#Calculando
if(x == 0):
	y = 0 #função
elif((x < 0 and x > -1) or ((x > 0) and (x < 1))):
	y = abs(x)
elif(x <= -1 or x >= 1):
	y = sqrt(abs(x))

#saída
print(round(y, 2))
	 