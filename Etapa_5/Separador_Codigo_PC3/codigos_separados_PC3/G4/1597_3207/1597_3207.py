from numpy import*
vet= array(eval(input()))
c= 0

while(c < size(vet)):
	if(vet[c]>80):
		vet[c] = vet[c] - vet[c]*(5/100)
	c= c+1
		
v1= sum(vet)
print(round(v1,2))