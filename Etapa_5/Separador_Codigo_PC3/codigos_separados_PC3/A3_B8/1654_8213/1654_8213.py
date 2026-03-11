from numpy import*
vetor=input("Digite: ").upper().split(",")
vz=zeros(5,dtype=int)
cont=0
for i in range(size(vetor)):
	if vetor[i]=="AM":
		vz[0]=vz[0]+1
		
	elif vetor[i]=="PE":
		vz[1]=vz[1]+1
		
	elif vetor[i]=="MG":
		vz[2]=vz[2]+1
		
	elif vetor[i]=="SP":
		vz[3]=vz[3]+1
		
	elif vetor[i]=="RS":
		vz[4]=vz[4]+1
print(max(vz))
print(vz)