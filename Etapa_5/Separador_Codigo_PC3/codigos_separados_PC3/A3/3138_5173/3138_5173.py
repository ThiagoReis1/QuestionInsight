from numpy import * 

vetorN = array(eval(input("entre com numeros: ")))

cont = 0 
media = 0 
total = 0 
N = size(vetorN)
#NM = size(vetorN)/sum(vetorN)

while(cont<size(vetorN)):
	media += vetorN[cont]**7
	
	cont += 1

total = (media/N)**(1/7)

print(round(total, 2))

