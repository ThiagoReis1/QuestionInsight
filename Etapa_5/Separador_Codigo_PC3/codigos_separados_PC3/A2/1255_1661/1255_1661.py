from numpy import *
vetor = array(eval(input("digite o vetor: ")))
vetor1 = array(zeros(2, dtype = int))
for i in range (0, size(vetor)):
	a = min(vetor)
	b = max(vetor)
c = (0.65 * a) + (0.35 * b)
d = (0.45 * a) + (0.55 * b)
cont = 0
for i in range (size(vetor)):
	if(vetor[i] >= a and vetor[i] < c):
		cont = cont + 1
	else:
		cont = cont
i = 0
cont1 = 0
while (i < size(vetor)):
		if (vetor[i] >= c and vetor[i] < d):
			cont1 = cont1 +1
			i = i + 1
		else:
			i = i + 1
			
vetor1[0] = cont
vetor1[1] = cont1
print(vetor1)
	