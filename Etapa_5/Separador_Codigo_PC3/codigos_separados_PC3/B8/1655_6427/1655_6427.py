from numpy import*
vetor_ent = input("vetor_ent: ").split(',')

vcont = zeros(5, dtype = int)

for i in range(size(vetor_ent)):
	if(vetor_ent[i] == "AC"):
		vcont [0] = vcont[0] + 1
	elif(vetor_ent[i] == "AM"):
		vcont[1] = vcont[1] + 1
	elif(vetor_ent[i] == "PA"):
		vcont[2] = vcont[2] + 1
	elif(vetor_ent[i] == "RO"):
		vcont[3] = vcont[3] +1
	elif(vetor_ent[i] == "RR"):
		vcont[4] = vcont[4] + 1
maior = 0

for i in vcont:
	if i > maior:
		maior = i
print(maior)		
print(vcont)

		