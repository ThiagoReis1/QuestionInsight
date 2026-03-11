from numpy import *

n = input(" ").split(",")
cont = zeros(4, dtype=int)

for i in n:
	if(i == "C"):
		cont[0] = cont[0] + 1
		
	elif(i == "D"):
		cont[1] = cont[1] + 1
		
	elif(i == "V"):
		cont[2] = cont[2] + 1
		
	elif(i == "U"):
		cont[3] = cont[3] + 1
print(cont)
		
	

	