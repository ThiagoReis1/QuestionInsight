from numpy import *

freq = array(eval(input("Frequencia: ")))

contaprov = 0

for i in range(size(freq)):
	if(freq[i] >= 70):
		contaprov = contaprov + 1

aprovados = zeros(contaprov, dtype = int)
j = 0
for i in range(size(freq)):
	if(freq[i] >= 70):
		aprovados[j] = i
		j = j + 1
			
print(contaprov)
print(aprovados)