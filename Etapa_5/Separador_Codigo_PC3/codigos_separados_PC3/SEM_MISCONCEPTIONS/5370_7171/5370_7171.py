#CRESCENTE
from numpy import*
vet= array(eval(input("Digite o vetor:")))

i=1
contf=0
contt=0
while(i<size(vet)):
	if (vet[i]>= vet[(i-1)]):
		contt= contt+1	
	else:
		contf=contf+1
	i=i+1
	
if(contt==(size(vet)- 1)):
	print("True")
else:
	print("False")
