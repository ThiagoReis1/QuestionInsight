from numpy import *

vetor1 = array(eval(input("Digite as distancias: ")))

recorde = 2.5
i = 0
k = 0
while(i < size(vetor1)):
	if(vetor1[i] > recorde):
		k = k + 1 
	i = i + 1
print(recorde)

print(k)
