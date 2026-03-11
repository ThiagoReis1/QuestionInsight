from numpy import*
vet=array(eval(input("digite a pontuacao")))
i=0
pont=0

while(size(vet)>i):
	if(vet[i]==1):
		pont=pont+80
	if(vet[i]==2):
		pont=pont+40
	if(vet[i]==3):
		pont=pont+20
	i=i+1
print(pont)
		
	