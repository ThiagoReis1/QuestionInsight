from numpy import *
v = input(": ").upper().split(',')

cont = zeros(6, dtype = int)

for I in range(size(v)):
	if(v[I] == "MC"):
		cont[0] = cont[0] + 1
	elif(v[I] == "C"):
		cont[1] = cont[1] + 1
	elif(v[I] == "CM"):
		cont[2] = cont[2] + 1
	elif(v[I] == "EM"):
		cont[3] = cont[3] + 1
	elif(v[I] == "E"):
		cont[4] = cont[4] + 1
	else:
		cont[5] = cont[5] + 1
print(max(cont))
print(cont)