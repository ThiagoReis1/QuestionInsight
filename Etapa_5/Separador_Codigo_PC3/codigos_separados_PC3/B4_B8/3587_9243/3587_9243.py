from numpy import *
v = array(eval(input("v:")))
pontos = 0
for x in v:
	if x == 1:
		pontos += 5
	elif x == 2:
		pontos += 3
	elif x == 3:
		pontos += 3
	elif x == 4:
		pontos += 2
print(pontos)
			
		
		
