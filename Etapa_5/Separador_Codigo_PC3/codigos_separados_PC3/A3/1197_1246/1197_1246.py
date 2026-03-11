#Karoline Oliveira da Costa
#11 de agosto de 2016
#Av.05 Questão 2
from numpy import*
vet_temp=array(eval(input("Digite as temperaturas: ")))

i=0
count=0
vetor=array(zeros(count,dtype=float))
while(i<size(vet_temp)):
	if(vet_temp[i]>50):
		count=count+1
	i=i+1
vetor_resultante=array(count, dtype=float)
while(i<size(vet_temp)):
	if(vet_temp[i]<50):
		vet_temp[i]=vetor_resultante[count]
		count=count+1
	i=i+1
print(vetor_resultante)
