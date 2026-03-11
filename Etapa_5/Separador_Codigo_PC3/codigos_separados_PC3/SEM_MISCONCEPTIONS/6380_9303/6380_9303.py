from numpy import *
caract = input("a: ").split(",")
cont = zeros(4, dtype=int)
for i in caract:
	if i == "E":
		cont[0] += 1
	elif i == "V":
		cont[1] += 1
	elif i == "A":
		cont[2] += 1
		
	else:
		cont[3] += 1
print(cont)