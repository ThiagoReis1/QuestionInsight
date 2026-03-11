from numpy import *

# entrada (saques)

saq = array(eval(input()))

# contadora

scont = 0 # valores altos de saque

# laço 1
 
for i in range(size(saq)):
	
	if (saq[i] >= 2000):
		
		scont = scont + 1
		
	

# saida 1

print (scont)

# vetor de saida 2

vets = zeros (scont, dtype = int)

# laço 2

for i in range (size(saq)):
	
	if (i == 0):
		
		u = 0 # datermina progressao do vetor saida 2
		
	if (saq[i] >= 2000):
		
		vets[u] = i
		u = u + 1
		
	

# saida 2

print (vets)