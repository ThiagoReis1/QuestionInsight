from numpy import *
notas = array(eval(input("Escreva notas: ")))
peso = array([3, 5, 1])
num = 0
den = sum(peso)
i = 0

while i < size(notas):
	num = num+ notas[i] * peso[i]
	i += 1

print(round(num / den, 2))
