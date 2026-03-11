from numpy import *

vetor = array(eval(input("Digite o vetor: ")))
A = min(vetor)
B = max(vetor)
i = 0
C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B
x = array(zeros(2, dtype =int))


while (i<size(vetor)):
	if ((vetor[i])>=A and vetor[i]< C):
		x[0] = x[0] + 1 
		
	if((vetor[i])>=C and vetor[i]< D):
		x[1]= x[1] + 1 
	i = i + 1
print (x)	
		
		
	