from numpy import*
from numpy.linalg import*

vet=array(eval(input("Digite um vetor para calcular a media: ")))

cont=0
M=1
for i in range(size(vet)):
	M=M*(vet[i])
	cont=cont+1
print(round(M**(1/cont),2))