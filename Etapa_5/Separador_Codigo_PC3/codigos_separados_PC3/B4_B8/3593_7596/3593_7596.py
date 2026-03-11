from numpy import *
valor = array(eval(input("valor: ")))
i = 0
pont = 200

while (i < size(valor)):
	if (valor[i] == 1):
		pont = pont / 2
	elif (valor[i] == 2):
		pont = pont * 3
	elif (valor[i] == 3):
		pont = pont / 2
	elif (valor[i] == 4):
		pont = pont * 3
	elif (valor[i] == 5):
		pont = pont / 2
	elif (valor[i] == 6):
		pont = pont * 3
	i = i + 1
	
print(pont)