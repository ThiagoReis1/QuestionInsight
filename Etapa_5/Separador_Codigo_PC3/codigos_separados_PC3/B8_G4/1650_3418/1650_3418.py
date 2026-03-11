from numpy import*
vet = input("").split(',')
cont = zeros (5, dtype=int)
for i in range(size(vet)):
	if(v[i]=="P"):
		cont[0] = cont[0]+1
	elif(v[i]=="C"):
		cont[1] = cont[1]+1
	elif(v[2]=="R"):
		cont[2] = cont[2]+1
	elif(v[3]=="L"):
		cont[3] = cont[3]+1
	elif(v[4]=="B"):
		cont[4] = cont[4]+1
print(max(cont))
print(cont)
