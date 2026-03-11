from numpy import * 

vetorNotas = array(eval(input("entre com notas ")))

cont = 0 
#notas2 = 0

while(cont<size(vetorNotas)):
	if(vetorNotas[cont] < 2):
		vetorNotas[cont] = 0  #vetorNotas[cont] == 0
		
	elif(vetorNotas[cont] > 8):
		vetorNotas[cont] =10  #vetorNotas[cont] == 10
		
	cont+= 1
	
print(vetorNotas)
		