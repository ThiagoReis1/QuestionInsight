from numpy import *
vet=input()
i=0
s=0

while(i<len(vet)):
	if(vet[i].lower()=='a' or vet[i].lower()=='e' or vet[i].lower()=='i'or vet[i].lower()=='o'or vet[i].lower()=='u'):
		s=s+0.15
	else:
		s=s+0.17
	i=i+1	
print(round(s,2))



