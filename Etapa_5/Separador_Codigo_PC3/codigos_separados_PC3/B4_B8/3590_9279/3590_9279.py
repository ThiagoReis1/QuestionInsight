from numpy import *
v = array(eval(input("v:")))
pontos = 0
for x in v:
	if x == 1:
		pontos += 10
	elif x == 2:
		pontos += 5
	elif x == 3:
		pontos += 0
	elif x == 4:
		pontos += 5
	elif x == 5:
		pontos += 20
	elif x == 6:
		pontos += 10
print(pontos)