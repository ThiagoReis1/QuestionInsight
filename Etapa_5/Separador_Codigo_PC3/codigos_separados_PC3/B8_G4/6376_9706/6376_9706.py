from numpy import *
cont = zeros(4,dtype=int)
vet = input().upper().split(",")
for i in vet:
	if i == "A":
		cont[0] = cont[0]+1
	elif i == "B":
		cont[1] = cont[1]+1
	elif i == "C":
		cont[2] = cont[2]+1
	elif i == "D":
		cont[3] = cont[3]+1
print(cont)