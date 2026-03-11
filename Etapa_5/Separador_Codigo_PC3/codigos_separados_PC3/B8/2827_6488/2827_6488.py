from numpy import *
from math import *

notas = array(eval(input("Digite as notas: ")))

quantidade = size(notas)
i = 0

while (i < quantidade):
	if (notas[i] >= 4) and (notas[i] <= 5):
		notas[i] = 4
	elif (notas[i] >= 9) and (notas[i] <= 10):
		notas[i] = 10
	i = i + 1
print(notas)