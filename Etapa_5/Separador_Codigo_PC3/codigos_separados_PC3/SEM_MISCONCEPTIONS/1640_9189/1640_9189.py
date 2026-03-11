from numpy import*

turmas = array ( eval ( input ( "digite: ")))
impar = 0
j=0

for i in range( size(turmas)):
	
	if turmas[i] % 2 != 0:
		impar += 1
print(impar)
		
vturma = zeros(impar,dtype=int)
	
for i in range( size(turmas)):
		
		if turmas[i] % 2 != 0:
			
			vturma[j] = i
			
			j = j + 1

print(vturma)
		


		
		
	
	