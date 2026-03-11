from numpy import*
vet1 = (input(": ")).split(',')
vet = zeros(4, dtype = int)
i=0
while(i<size(vet1)):
	if(vet1[i] == "AR"):
		vet[0]=vet[0]+1
		i=i+1
	elif(vet1[i]=="BR"):
		vet[1]=vet[1]+1
		i=i+1
	elif(vet1[i]=="CL"):
		vet[2]=vet[2]+1
		i=i+1
	elif(vet1[i]=="CO"):
		vet[3]=vet[3]+1
		i=i+1
	elif(vet1[i]=="UY"):
		vet[4]=vet[4]+1
		i=i+1
print(vet)
