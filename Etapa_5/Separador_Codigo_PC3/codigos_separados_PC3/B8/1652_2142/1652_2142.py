from numpy import *

cont = zeros(5, dtype = int)
etnia = input("Digite as etnias: ").split(',')

for i in range(size(etnia)):
	if(etnia[i] == "B"):
		cont[0] = cont[0] + 1
	elif(etnia[i] == "PA"):
		cont[1] = cont[1] + 1
	elif(etnia[i] == "PR"):
		cont[2] = cont[2] + 1
	elif(etnia[i] == "A"):
		cont[3] = cont[3] + 1
	elif(etnia[i] == "I"):
		cont[4] = cont[4] + 1
x = max(cont)
print(x)
print(cont)