from numpy import *
v = input("Paises: ").split(',')
cont = zeros(5, dtype=int)

for i in range(size(v)):
	if (v[i] == "CHN"):
		cont[0] = cont[0] + 1
	elif (v[i] == "JPN"):
		cont[1] = cont[1] + 1
	elif (v[i] == "KOR"):
		cont[2] = cont[2] + 1
	elif (v[i] == "MGL"):
		cont[3] = cont[3] + 1
	elif (v[i] == "THA"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)