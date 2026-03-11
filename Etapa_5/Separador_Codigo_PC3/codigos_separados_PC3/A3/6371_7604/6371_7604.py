from numpy import*

numero = array(eval(input("insira o numero: ")))
cont = 0


for i in range(size(numero)):
	if numero [i] == 0 :
	   numero[i] = (9**2) 
	else:
		numero [i] = (numero [i] -1)**2
		
print(numero)