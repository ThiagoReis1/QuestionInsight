from numpy import*
vet= array((eval(input("Digite as notas:"))))
ap=0

for i in range (size(vet)):
	if (vet[i]>=5):
		ap+=1
cont= zeros(ap, dtype=int)

for i in range (size(vet)):
	if (vet[i]== ap):
		cont[i]= cont[ap]
		
print(ap)
print(cont)

	
