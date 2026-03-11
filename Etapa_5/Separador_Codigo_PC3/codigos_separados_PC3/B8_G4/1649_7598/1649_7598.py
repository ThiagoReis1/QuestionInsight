from numpy import*

co = input("cor dos olhos").split(",")
cont = zeros(5,dtype=int)

for i in range(size(co)):
	if("P" == co[i]):
		cont[0] = cont[0] + 1
	elif("C" == co[i]):
		cont[1] = cont[1] + 1
	elif("M" == co[i]):
		cont[2] = cont[2] + 1
	elif("V" == co[i]):
		cont[3] = cont[3] + 1
	elif("A" == co[i]):
		cont[4] = cont[4] + 1

print(max(cont))
print(cont)



		

	

