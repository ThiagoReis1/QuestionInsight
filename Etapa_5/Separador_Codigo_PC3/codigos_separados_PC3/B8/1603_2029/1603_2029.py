from numpy import *

vet = array(eval(input("aneis acertados pelo jogador: ")))
pontos = 0

while( 4 < size(vet)):
	if(size(vet) == 1):
		pontos = pontos + 80
	elif(size(vet) == 2):
		pontos = pontos + 40
	elif(size(vet) == 3):
		pontos = pontos + 20
print(pontos)
	
