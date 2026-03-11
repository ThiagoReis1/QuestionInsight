from numpy import *
arcos= array(eval(input("Insira o conj de vetores:")))
i= 0 
pontos= 10000

while i < size(arcos):
	if arcos[i]== 1:
		pontos= pontos * 2
	elif arcos[i]== 2:
		pontos= pontos
	elif arcos[i]== 3:
		pontos= pontos/2
	elif arcos[i]== 4:
		pontos= pontos/4
	i= i + 1

print(round(pontos,2))
