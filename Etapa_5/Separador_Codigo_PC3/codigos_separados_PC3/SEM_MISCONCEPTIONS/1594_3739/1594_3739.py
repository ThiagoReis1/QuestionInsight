# Leitura do vetor ataques
ataques = input("Informe os ataques:").upper()           
while (i< len(ataques)):
if(ataques[i] == "p"):
   danos = danos + 20
elif (ataques[i] == "v"):
   danos = danos + 8
i = i+ 1
while(danos[i] !=max(danos)):
i = i+ 1
elif(vet[i] == 'C'):
		cont[3] = cont[3] + 1
	elif(vet[i] == 'UY'):
		cont[4] = cont[4] + 1
print (cont)
for i in range(size(vet)):
	if (vet[i] % 2 == 2):
		vet= vet + 1
		print(vet)
print(danos)