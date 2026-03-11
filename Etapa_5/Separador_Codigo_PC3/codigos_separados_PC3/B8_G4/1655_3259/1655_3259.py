from numpy import *
cid = input("Cidades: ")
vet = cid.split(",")
i = 0
AC = 0
AM = 0
PA = 0
RO = 0
RR = 0
cont = zeros((1,5), dtype=int)
while i<size(vet):
	if vet[i] == "AC":
		cont[0,0] = AC + 1
	elif vet[i]=="AM":
		cont[0,1] = AM + 1
	elif vet[i]=="PA":
		cont[0,2] = PA + 1
	elif vet[i]=="RO":
		cont[0,3] = RO + 1
	elif vet[i]=="RR":
		cont[0,4] = RR + 1
	i = i + 1
print(vet)
#cont[0,0] = AC
#cont[0,1] = AM
#cont[0,2] = PA
#ont[0,3] = RO
#cont[0,4] = RR
print(cont)