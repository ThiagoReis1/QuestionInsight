from numpy import *

v=input().split(',')
vet=zeros(5,dtype=int)
		  
cont=0
for i in range(size(v)):
	if(v[i]=="CHN"):
		vet[0]=vet[0]+1	
	elif(v[i]=="JPN"):
		vet[1]=vet[1]+1	
	elif(v[i]=="KOR"):
		vet[2]=vet[2]+1	
	elif(v[i]=="MGL"):
		vet[3]=vet[3]+1	
	elif(v[i]=="THA"):
		vet[4]=vet[4]+1	
		  
maior=-1	 
for i in range(size(vet)):
	if(vet[i]>maior):
		maior=i
	

print(vet[maior])
print(vet)

#for i in range(size(vet)):
	