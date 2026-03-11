from numpy import*
v =input("").split(',')
cont = zeros(4, dtype = int)

for i in range(len(v)):
	if (v[i] == "O"):
		cont[0] = cont[0] + 1
	elif (v[i] == "D"):
		cont[1] = cont[1] + 1
	elif (v[i] == "N"):
		cont[2] = cont[2] + 1
	elif (v[i] == "C"):
		cont[3] = cont[3] + 1
print(cont)


		