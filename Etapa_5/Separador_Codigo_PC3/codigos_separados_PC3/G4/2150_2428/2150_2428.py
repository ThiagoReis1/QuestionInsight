from numpy import*



vet = array(eval(input()))
vet2 = zeros(4,dtype=int)
for i in vet:
	if (i == "BOTAFOGO"):
		vet2[0] = vet2[0] + 1
	elif (i == "FLAMENGO"):
		vet2[1] = vet2[1] + 1
	elif (i == "FLUMINENSE"):
		vet2[2] = vet2[2] + 1
	elif (i == "VASCO"):
		vet2[3] = vet2[3] + 1
	else:
		vet2[4] = vet2[4] + 1

print(vet2)