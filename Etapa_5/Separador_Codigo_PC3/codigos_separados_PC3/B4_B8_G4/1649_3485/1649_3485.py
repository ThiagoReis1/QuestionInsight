from numpy import*

vet = array(input("Cor: "))

for x in vet:
	if(x == "P"):
		x[vet] = x[vet] + 1 
	elif(x == "C"):
		x[vet] = x[vet] + 1 
	elif(x == "M"):
		x[vet] = x[vet] + 1 
	elif(x == "V"):
		x[vet] = x[vet] + 1 
	elif(x == "A"):
		x[vet] = x[vet] + 1 
print(max(vet))
print(vet)
		