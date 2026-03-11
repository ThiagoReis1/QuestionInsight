from numpy import*
vet=array(eval(input("Passageiros: ")))
p=0
t=size(vet)
i=0
for i in range(0,t):
	if(p>75):
		if(p-vet[i]<=75):
			p=p-vet[i]
			p=p+(p-vet[i])
	elif(vet[i]>0 and p<75):
		p=p+vet[i]
		
			
			
			
	if(vet[i]<0):
		p=p+vet[i]
	print(p)
	
		
		
print(p)