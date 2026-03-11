from numpy import *

alvos = array(eval(input()))
a1 = 100
a2 = 60
a3 = 20
a4 = 0
i = 0
pontos = 0

while i < len(alvos):
	if alvos[i] == 1:
		pontos += a1
	elif alvos[i] == 2:
		pontos += a2
	elif alvos[i] == 3:
		pontos += a3
	elif alvos[i] == 4:
		pontos += a4
	i += 1
print(pontos)
