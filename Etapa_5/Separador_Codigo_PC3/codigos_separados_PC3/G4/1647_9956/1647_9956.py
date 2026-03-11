from numpy import*
vet=array(eval(input()))
ap=0
for i in range(0,size(vet)):
	if vet[i] >= 70:
		ap += 1
		
aux= zeros(ap,dtype=int)
j=0
for i in range(0,size(vet)):
	if vet[i] >=70:
		aux[j]= i
		j += 1
print(ap)
print(aux)