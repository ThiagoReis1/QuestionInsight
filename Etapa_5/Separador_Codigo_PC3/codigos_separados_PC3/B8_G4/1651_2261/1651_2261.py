from numpy import *

p = input(":").upper().split(",")

cont = zeros(6,dtype = int)

for x in range(size(p)):
	if(p[x] == "MC"):
		cont[0] = cont[0] + 1
	elif(p[x] == "C"):
		cont[1] = cont[1] + 1
	elif(p[x] == "CM"):
		cont[2] = cont[2] + 1
	elif(p[x] == "EM"):
		cont[3] = cont[3] + 1
	elif(p[x] == "E"):
		cont[4] = cont[4] + 1
	elif(p[x] == "ME"):
		cont[5] = cont[5] + 1
print(max(cont))
print(cont)
		
		
		
		