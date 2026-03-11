from numpy import*

vet = input("").upper().split(",")
cont = zeros(5, dtype = int)

for i in vet: 
	if i == "AM":
		cont[0]+=1
	elif i == "PE":
		cont[1]+=1
	elif i == "MG":
		cont[2]+=1
	elif i == "SP": 
		cont[3]+=1
	elif i == "RS":
		cont[4]+=1
print(max(cont))
print(cont)
	