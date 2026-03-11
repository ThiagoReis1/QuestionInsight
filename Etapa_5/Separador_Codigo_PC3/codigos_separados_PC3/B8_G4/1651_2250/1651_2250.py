from numpy import *
v = input("v:").upper().split(',')
cont = zeros(6, dtype=int)
for x in range(size(v)):
	if(v[x] == "MC"):
		cont[0] = cont[0] + 1
	elif(v[x] == "C"):
		cont[1] = cont[1] + 1
	elif(v[x] == "CM"):
		cont[2] = cont[2] + 1
	elif(v[x] == "EM"):
		cont[3] = cont[3] + 1
	elif(v[x] == "E"):
		cont[4] = cont[4] + 1
	elif(v[x] == "ME"):
		cont[5] = cont[5] + 1
print(max(cont))
print(cont)