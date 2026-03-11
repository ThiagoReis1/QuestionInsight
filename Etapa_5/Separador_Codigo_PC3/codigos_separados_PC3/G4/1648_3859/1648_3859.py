#Reprovados por frequencia

from numpy import *

freq = array(eval(input("Frequencia: ")))
				 
repro = 0
for i in range(size(freq)):
	if freq[i] < 70:
		repro = repro + 1
n = zeros(repro, dtype = int)
j = 0
for i in range(size(freq)):
	if freq[i] < 70:
		n[j] = i
		j = j+1
	
print(repro)
print(n)		