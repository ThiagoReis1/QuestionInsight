from numpy import*
vet=array(eval(input("Notas: ")))
ap=0
for i in range(size(vet)):
	if vet[i]>=5:
		ap=ap+1
vet2=zeros(ap,dtype=int)
j=0
for i in range(size(vet)):
	if vet[i]>=5:
		vet2[j]=i
		j=j+1
print(ap)
print(vet2)