from numpy import*
v = input("").upper()
vet = zeros(size(v), dtype=int)
cont = 0
for i in vet:
	if (vet[i]=="A" or vet[i]=="E" or vet[i]=="I" or vet[i]=="O" or vet[i]=="U"):
		cont = cont+3.15
	else:
		cont = cont+4.17
		
print(round(cont))

