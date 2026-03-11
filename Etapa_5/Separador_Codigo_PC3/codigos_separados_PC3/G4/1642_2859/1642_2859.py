from numpy import *

vet = array(eval(input(" ")))

a = 0

for i in vet:
	if(i % 5 == 0):
		a = a + 1

v = zeros(a, dtype=int)
e = 0

for x in range(size(vet)):
	if( vet[x]% 5 == 0):
		v[e] = x
		e = e + 1		

print(a)
print(v)
		
	
	
	

		
		
		