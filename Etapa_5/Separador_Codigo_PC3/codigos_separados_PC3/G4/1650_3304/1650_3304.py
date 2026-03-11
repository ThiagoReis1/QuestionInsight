from numpy import*

cab = input("")
v = cab.split(',')
vet = zeros(5, dtype=int)

for cont in v:
	if(cont.upper() == "P"):
		vet[0] = vet[0]+1
	if(cont.upper() =="C" ):
		vet[1] = vet[1]+1
	if(cont.upper() == "R"):
		vet[2] = vet[2]+1
	if(cont.upper()=="L"):
		vet[3] = vet[3]+1
	if(cont.upper() == "B"):
		vet[4] = vet[4]+1
	
print(max(vet))
print(vet)