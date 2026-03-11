from numpy import*
cont = zeros(4,dtype=int)
vet = input("Contagem: ").upper().split()
for x in vet:
	if x == 'E':
		cont[0] = cont[0]+ 1
	elif x == 'V':
		cont[1] = cont[1] + 1
	elif x == 'A':
		cont[2] = cont[2]+1
	elif x == 'D':
		cont[3] = cont[3] +1
			
print(cont)