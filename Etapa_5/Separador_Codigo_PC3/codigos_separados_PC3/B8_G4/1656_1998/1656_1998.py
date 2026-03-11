from numpy import*
v1 = input("vetor:").split(",")
cont = zeros(5,dtype=int)
for i in range(len(v1)) :
	if v1[i] == "BE" :
		cont[0] = cont[0] + 1
	elif v1[i] == "ES" :
		cont[1] = cont[1] + 1
	elif v1[i] == "FR" :
		cont[2] = cont[2] + 1
	elif v1[i] == "IT" :
		cont[3] = cont[3] + 1
	elif v1[i] == "PT" :
		cont[4] = cont[4] + 1
print (max(cont))
print (cont)