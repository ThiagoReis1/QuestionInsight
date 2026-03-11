from numpy import* 
cont = zeros(5, dtype=int) 
vet = input("").split(",") 
for i in vet:
	if(i == "AR"):
		cont[0] = cont[0] + 1 
	elif(i == "BR") :
	 	cont[1] = cont[1] + 1 
	elif(i == "CL"): 
		cont[2] = cont[2] + 1
	elif( i== "CO"):
		cont[3] = cont[3] + 1 
	elif(i == "UY"):
		cont[4] = cont[4] + 1 
print(max(cont)) 
print(cont)