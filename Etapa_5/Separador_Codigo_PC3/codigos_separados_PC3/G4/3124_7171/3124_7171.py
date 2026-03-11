#geometrica
from numpy import*

vet=array(eval(input("Digite o vetor:")))
med= vet[0]

for i in range(1,size(vet)):
	med= med*vet[i] 
med= med**(1/size(vet))
print(round(med,2))
	
	
	