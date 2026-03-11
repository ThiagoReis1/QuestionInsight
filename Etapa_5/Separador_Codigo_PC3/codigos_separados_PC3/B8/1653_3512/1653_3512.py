from numpy import*
pele= input("Digite: ")
vetor= pele.split(',')
vet_resp = zeros(5, dtype=int)
for cont in vetor:
	if cont.upper()== "AR":
		vet_resp[0] = vet_resp[0] + 1
	elif cont.upper()== "BR":
		vet_resp[1] = vet_resp[1] + 1
	elif cont.upper()== "CL":
		vet_resp[2] = vet_resp[2] + 1
	elif cont.upper()== "CO":
		vet_resp[3] = vet_resp[3] + 1
	elif cont.upper()== "UY":
		vet_resp[4] = vet_resp[4] + 1
	
		
print(max(vet_resp))
print(vet_resp)


