from numpy import *
faces = array(eval(input()))
i = 0
pontos = 0
while i < 6:
	if faces == 1 or 3 or 5:
		pontos = pontos + 10
		i += 1
	
