from numpy import *
n = array(eval(input(" ")))
numeros = []
for x in n:
	if x == 9:
		numeros.append(0)
	else:
		numeros.append((x + 1) ** 3)
		
print("["+" ".join(map(str, numeros)) + "]")
