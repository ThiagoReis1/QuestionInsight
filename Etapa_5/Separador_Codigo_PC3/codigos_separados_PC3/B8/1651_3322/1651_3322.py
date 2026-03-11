from numpy import *
pele = input()
vetor = pele.split(',')
vet_resp = zeros(6, dtype=int)
for cont in vetor:
	if cont.upper()=="MC":
		vet_resp[0]=vet_resp[0] + 1
	elif cont.upper()=="C":
		vet_resp[1]=vet_resp[1] + 1
	elif cont.upper()=="CM":
		vet_resp[2]=vet_resp[2] + 1
	elif cont.upper()=="EM":
		vet_resp[3]=vet_resp[3] + 1
	elif cont.upper()=="E":
		vet_resp[4]=vet_resp[4] + 1
	elif cont.upper()=="ME":
		vet_resp[5]=vet_resp[5] + 1
print(max(vet_resp))
print(vet_resp)