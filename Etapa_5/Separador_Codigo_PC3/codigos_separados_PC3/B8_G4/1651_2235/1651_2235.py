from numpy import*

p=input("Cor da pele: ").split(',')

cont=zeros(6,dtype=int)
for i in p:
	if(i.upper() == "MC"):
		cont[0] = cont[0] + 1
	elif(i.upper() == "C"):
		cont[1] = cont[1] + 1
	elif(i.upper() == "CM"):
		cont[2] = cont[2] + 1
	elif(i.upper() == "EM"):
		cont[3] = cont[3] + 1
	elif(i.upper() == "E"):
		cont[4] = cont[4] + 1
	elif(i.upper() == "ME"):
		cont[5] = cont[5] + 1
			
print(max(cont))
print(cont)