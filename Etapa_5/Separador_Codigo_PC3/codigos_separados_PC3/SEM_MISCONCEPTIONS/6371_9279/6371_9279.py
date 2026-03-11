from numpy import *
v = array(eval(input("v: ")))
numeros = []
for x in v:
	if x == 0:
		numeros.append(9 ** 2)
	else:
		numeros.append((x - 1) ** 2)
print("[" + " ".join(map(str, numeros)) + "]")