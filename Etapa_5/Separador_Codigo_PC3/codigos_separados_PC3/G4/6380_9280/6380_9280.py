from numpy import *
p = input("P: ").split(",")
cont = zeros(4, dtype=int)
for x in p:
	if x == 'E':
		cont[0] += 1
	elif x == 'V':
		cont[1] += 1
	elif x == 'A':
		cont[2] += 1
	else:
		cont[3] += 1
print(cont)