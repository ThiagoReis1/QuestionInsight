from numpy import * 

vetorLado = array(eval(input("entre com o lado do dado: ")))

cont = 0 
acumulador = 0 

while(cont<size(vetorLado)):
	if(vetorLado[cont] == 1):
		acumulador = (acumulador+ 10)
	elif(vetorLado[cont] == 2):
		acumulador = (acumulador + 5)
	elif(vetorLado[cont] == 3):
		acumulador = (acumulador+ 10)
	elif(vetorLado[cont] == 4):
		acumulador = (acumulador+ 5)
	elif(vetorLado[cont] == 5):
		acumulador = (acumulador+ 10)
	elif(vetorLado[cont] == 6):
		acumulador = (acumulador+ 5)
	
	cont += 1
	
print(acumulador)