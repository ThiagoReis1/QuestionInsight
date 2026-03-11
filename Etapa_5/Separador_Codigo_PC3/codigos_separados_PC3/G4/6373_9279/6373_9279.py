from numpy import *
s = input("s: ").split(",")
cont = zeros(4, dtype=int)
for x in s:
	if x == "A":
		cont[0] += 1
	elif x == "P":
		cont[1] += 1
	elif x == "D":
		cont[2] += 1
	else:
		cont[3] += 1
print(cont)	