from numpy import *
notas = array(eval(input("Notas: ")))

i = 0
while(i < size(notas)):
	if(notas[i] < 5 and notas[i] > 4):
		notas[i] =4
	elif(notas[i] < 10 and notas [i] > 9):
		notas[i] =10
	i = i + 1
print(notas)