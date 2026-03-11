from numpy import*

cod = input("Codigo: ").split(',')

cont = zeros(5,dtype=int)



for i in range(len(cod)):
	if (cod[i] == "B"):
		cont[0] = cont[0] + 1
	elif (cod[i] == "PA"):
		cont[1] = cont[1] + 1
	elif (cod[i] == "PR"):
		cont[2] = cont[2] + 1
	elif (cod[i] == "A"):
		cont[3] = cont[3] + 1
	elif (cod[i] == "I"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)