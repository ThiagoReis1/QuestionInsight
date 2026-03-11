from numpy import*
vet1=array(eval(input("Digite as notas: ")))
vet2=vet1
i=0
while(i<size(vet1)):
	if(vet1[i]>8):
		vet2[i]=10
	elif(vet1[i]<2):
		vet2[i]=0
	i=i+1
print(vet2)