from numpy import*

vetor=array(eval(input("Tempo: ")))
a=max(vetor)
#print(i)

i=0
cont=0
while(vetor[i] != a):
	cont=cont+1
	i=i+1

print(cont)