from numpy import *

n = array(eval(input()))

# variavel loop

i = 0 # percorrer o vetor notas

while (i < size(n)):
	
	if (n[i] > 8):
		
		n[i] = 10
		
	if (n[i] < 2):
		
		n[i] = 0
		
	
	i = i + 1
	

print (n)