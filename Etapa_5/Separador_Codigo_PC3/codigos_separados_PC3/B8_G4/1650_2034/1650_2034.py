from numpy import*

cor= input("cor:").upper().split(',') 
vet2= zeros(5,dtype=int)

for i in range(size(cor)):
	if(cor[i]=="P"):
		vet2[0]=vet2[0] +1
	elif(cor[i]=="C"):	
		vet2[1]=vet2[1] +1
	elif(cor[i]=="R"):
		vet2[2]=vet2[2] +1
	elif(cor[i]=="L")	:
		vet2[3]=vet2[3] +1
	elif(cor[i]=="B")	:
		vet2[4]=vet2[4] +1
		
print(max(vet2))
print(vet2)
	
	
	

	