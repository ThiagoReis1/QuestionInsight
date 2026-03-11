from numpy import *

jogadas = array(eval(input()))
pontos = 200.0
i = 0

while(i < size(jogadas)):
	face = jogadas[i]
	if(face == 1 or face == 3 or face == 5):
		pontos /= 2
	elif(face == 2 or face == 4 or face == 6):
		pontos *= 3
	i+=1 
print(round(pontos,2))