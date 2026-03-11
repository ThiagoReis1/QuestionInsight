from numpy import *

pcte = input('').upper().split(',')
cont = zeros(4, dtype=int)


for v in pcte:
	if v == "O":
		cont[0] +=1
	elif v == "D":
		cont[1] +=1
	elif v == "N":
		cont[2] +=1
	elif v == "C":
		cont[3] +=1
print(cont)