from numpy import*

vet=input("digite os paises: ").split(',')

vet2=zeros(5, dtype=int)



for i in range(len(vet)):
	
	if(vet[i].upper()=="BE"):
		vet2[0]=vet2[0]+1
	elif(vet[i].upper()=="ES"):
		vet2[1]=vet2[1]+1
	elif(vet[i].upper()=="FR"):
		vet2[2]=vet2[2]+1
	elif(vet[i].upper()=="IT"):
		vet2[3]=vet2[3]+1
	elif(vet[i].upper()=="PT"):	
		vet2[4]=vet2[4]+1
		
		
print(max(vet2))
print(vet2)