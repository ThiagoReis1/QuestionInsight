from math import *
from numpy import *

freq = array(eval(input("Frequencia: ")))
				 

cont = 0
				 
for i in range(size(freq)):
	if freq[i] < 70:
		cont = cont + 1

indice = zeros(cont, dtype = int)
m = 0		 
for j in range(size(freq)):
	if freq[j] < 70:
		indice[m] = j
		m = m + 1
				 
print(cont)
print(indice)
