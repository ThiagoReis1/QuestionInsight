from numpy import*

vetor =  array(eval(input("Temperaturas: ")))
i = 0
r = 0
while ( i<size(vetor)):
	if vetor[i]< 50 :
		r = r + 1
	i = 1 + i
vetor1 = array(zeros(r, dtype = float))
i = 0 
j = 0
while ( i < size(vetor)):
	if (vetor[i]<50):
		vetor1[j] = vetor[i]
		j = 1 + j
	i = i + 1

print(vetor1)