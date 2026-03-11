from numpy import*

vetor= array(eval(input("Temperaturas: ")))

i=0
j=0
while( i < size(vetor)):
	if (vetor[i] < 0):
		j=j + 1
	i=i+1

vetor1=array(zeros(size(vetor)-j,dtype=float))			

i=0
j=0
while( i < size(vetor)):
	if (vetor[i] >= 0):
		vetor1[j] = vetor[i]
		j=j+1
	i=i+1	

print(vetor1)	
	

