from numpy import *

notas = array(eval(input(": ")))

n = 0
v = 0
while n < size(notas):
	if notas[n] > 4 and notas[n] < 5:
		notas[n] = 4
	elif notas[n] > 9 and notas[n] < 10:
		notas[n] = 10
	n = n + 1
print(notas)
	