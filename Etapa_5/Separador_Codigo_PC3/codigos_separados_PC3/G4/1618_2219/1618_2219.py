from numpy import*
 
coeficientes = array(eval(input("Informe os coeficientes:")))

x = ''

i = 0
while (i<size(coeficientes)):
	if (i < (size(coeficientes)-2)):
		tam = size(coeficientes)
		x = x + str(coeficientes[i]) + ("x^") + str(tam -(i+1)) + " + "
	elif (i == (size(coeficientes)-1)):
		tam = size(coeficientes)
		x = x + str(coeficientes[i]) + ("x")  + " + "
	else:
		x = x + str(coeficientes[i])
	
	i = i+1
print(x)
	