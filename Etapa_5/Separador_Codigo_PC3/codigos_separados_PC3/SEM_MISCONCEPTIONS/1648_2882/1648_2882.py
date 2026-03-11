from numpy import*

vetor=array(eval(input("Frequencia: ")))


cont=0

for i in range(size(vetor)):
	if(vetor[i]<70):
		cont=cont+1
		
print(cont)

ind=zeros(size(vetor),dtype=int)

for i in range(size(vetor)):
	if(vetor[i]<70):
		ind[i]=ind[i]+[i]


print((ind))


	
	
	