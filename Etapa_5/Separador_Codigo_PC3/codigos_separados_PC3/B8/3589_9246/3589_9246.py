from numpy import *

v = array(eval(input("digite:")))
pontos = 0

for x in v:
	if x == 1:
		pontos += 80
	elif x == 2:
		pontos += 40
	elif x == 3:
		pontos += 20
	elif x == 4:
		pontos += 10
	
print(pontos)