from numpy import*
vet=array(eval(input("")))
v1=min(vet)
i=0
while(i<size(vet)):
	if(vet[i]==v1):
		vet[i]=0
	i=i+1
M=(sum(vet))/3

print(round(M,2))
if(M>=5.0):
	print("APROVOU")
else:
	print("REPROVOU")



