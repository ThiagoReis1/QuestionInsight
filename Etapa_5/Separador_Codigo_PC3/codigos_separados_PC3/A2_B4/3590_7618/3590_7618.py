from numpy import *

face=eval(input("digite a face do dado= "))

i= 0 
pontos= 0

while i < size(face):
	if face[i] == 1:
		pontos = pontos + 10 
	elif face[i] == 2:
		pontos= pontos + 5
	elif face[i]== 3:
		pontos= pontos
	elif face[i] == 4:
		pontos= pontos + 5
	elif face[i]== 5:
		pontos=pontos + 20
	else:
		pontos= pontos + 10
	i= i + 1
print(pontos)