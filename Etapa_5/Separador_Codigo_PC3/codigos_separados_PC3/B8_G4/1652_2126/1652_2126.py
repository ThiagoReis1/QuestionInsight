from numpy import*

vet = input("Uma string:").split(',')

vet2 = zeros(5, dtype=int)

for i in vet:
	if i.upper()=="B":
		vet2[0]=vet2[0]+1
	elif i.upper()=="PA":
		vet2[1]=vet2[1]+1
	elif i.upper()=="PR":
		vet2[2]=vet2[2]+1
	elif i.upper()=="A":
		vet2[3]=vet2[3]+1
	elif i.upper()=="I":
		vet2[4]=vet2[4]+1

print(max(vet2))
print(vet2)		
		
		