from numpy import*

anel = array(eval(input("Valor do anel: ")))

acumulador = 0
cont = 0

while cont < (size(anel)):
	if anel [cont] == 1 :
		acumulador = acumulador + 100
	elif anel [cont]  == 2 :
		acumulador = acumulador + 60
	elif anel [cont] == 3 :
		acumulador = acumulador + 20
	elif anel [cont] == 4 : 
		acumulador = acumulador + 0	
	cont = cont + 1
print(acumulador)