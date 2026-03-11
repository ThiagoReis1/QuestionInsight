from numpy import*
vet=array(eval(input("digite os pesos:")))
r = 307
mr=0
i=0
while(i<size(vet)):
	if(vet[i]<r):
	   mr=mr+1
	i=i+1
print(r)
print(mr)
