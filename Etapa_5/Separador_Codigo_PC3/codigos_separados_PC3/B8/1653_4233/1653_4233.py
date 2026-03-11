from numpy import*

string = input("Digite: ").split(",")

	
cont = zeros(5, dtype=int)

for i in range(len(string)):
	if(string[i]=="AR"):
		cont[0] = cont[0] + 1
	elif(string[i]=="BR"):
		cont[1] = cont[1] + 1
	elif(string[i]=="CL"):
		cont[2] = cont[2] + 1
	elif(string[i]=="CO"):
		cont[3] = cont[3] + 1
	elif(string[i]=="UY"):
		cont[4] = cont[4] + 1
		

print(max(cont))
print(cont)
	