from numpy import *

v = input("v:").upper().split(',')
cont = zeros(5, dtype = int)

for x in range(size(v)):
	if(v[x] == "BE"):
		cont[0] = cont[0] + 1
	elif(v[x] == "ES"):
		cont[1] = cont[1] + 1
	elif(v[x] == "FR"):
		cont[2] = cont[2] + 1
	elif(v[x] == "IT"):
		cont[3] = cont[3] + 1
	elif(v[x] == "PT"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
		
		

		

