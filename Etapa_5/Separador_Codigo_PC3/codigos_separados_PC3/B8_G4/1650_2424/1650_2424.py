from numpy import *
v = input("v:").upper().split(',')
cont = zeros(5, dtype = int)
for x in range(size(v)):
	if(v[x] == "P"):
		cont[0] = cont[0] + 1
	elif(v[x] == "C"):
		cont[1] = cont[1] + 1
	elif(v[x] == "R"):
		cont[2] = cont[2] + 1
	elif(v[x] == "L"):
		cont[3] = cont[3] + 1
	elif(v[x] == "B"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)


