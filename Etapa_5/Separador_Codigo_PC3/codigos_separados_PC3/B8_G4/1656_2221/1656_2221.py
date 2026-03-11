from numpy import*

z=input("Digita ai: ").split(',')

cont=zeros(5, dtype=int)

for i in z:
	if(i.upper() == "BE"):
		cont[0] = cont[0] + 1
	elif(i.upper() == "ES"):
		cont[1] = cont[1] + 1
	elif(i.upper() == "FR"):
		cont[2] = cont[2] + 1
	elif(i.upper() == "IT"):
		cont[3] = cont[3] + 1
	elif(i.upper() == "PT"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)


		
