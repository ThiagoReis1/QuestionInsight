from numpy import *
vetor=array(eval(input("Informe o vetor:")))
A=min(vetor)
B=max(vetor)
C=0.6*A+0.4*B
D=0.3*A+0.7*B
vet2=array(zeros(2,dtype=int))
i=0
x1=0
x2=0
while(i<size(vetor)):
	if(vetor[i]>=C and vetor[i]<D):
		x1=x1+1
		vet2[0]=x1
	elif(vetor[i]>=D and vetor[i]<B):
		x2=x2+1
		vet2[1]=x2
	i=i+1
print(vet2)