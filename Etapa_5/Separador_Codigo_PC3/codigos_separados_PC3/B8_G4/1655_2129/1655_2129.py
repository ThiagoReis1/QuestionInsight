from numpy import*

vet = input("digite o estado: ").split(',')
cont = zeros(5,dtype=int)
for elemento in vet:
	if(elemento == "AC"):
		cont[0] = cont[0]+1
	elif(elemento == "AM"):
		cont[1] = cont[1]+1
	
	elif(elemento == "PA"):
		cont[2] = cont[2]+1
	
	elif(elemento == "RO"):
		cont[3] = cont[3]+1
		
	elif(elemento == "RR"):
		cont[4] = cont[4]+1
		
print(max(cont))
print(cont)		
		