from numpy import*
cont = zeros(4,dtype=int)
v = input("").upper().split(",")
for i in range(size(v)):
	if (v[i] == "C" ):
		cont[0] = cont[0] + 1 
	elif (v[i] == "O"):
		cont[1] = cont[1] + 1
	elif (v[i] == "P"):
		cont[2] = cont[2] + 1
	else:
		v[i] == "E"
		cont[3] = cont[3] + 1
print(cont)
		
	
	
	
