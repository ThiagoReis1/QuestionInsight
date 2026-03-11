from numpy import *
a = input("A:").split(",")
cont = zeros(4 ,dtype=int)
for x in a:
	if x == "P":
		cont[0] += 1
	elif x == "D":
		cont[1] += 1
	elif x == "M":
		cont[2] += 1
	else:
		cont[3] += 1
print(cont)
