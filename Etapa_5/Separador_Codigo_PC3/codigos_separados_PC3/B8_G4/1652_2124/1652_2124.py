from numpy import*

vet=input("Digite um vet:").split(',')

vet2= zeros(5, dtype=int)

for elemento in vet:
	if elemento.upper()=="B":
		vet2[0]=vet2[0]+1
	elif elemento.upper()=="PA":
		vet2[1]=vet2[1]+1
	elif elemento.upper()=="PR":
		vet2[2]=vet2[2]+1
	elif elemento.upper()=="A":
		vet2[3]=vet2[3]+1
	elif elemento.upper()=="I":
		vet2[4]=vet2[4]+1
		
print(max(vet2))
print(vet2)