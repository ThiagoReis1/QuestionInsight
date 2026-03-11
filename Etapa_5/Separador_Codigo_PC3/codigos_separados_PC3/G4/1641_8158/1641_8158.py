from numpy import *

v = array(eval(input("Digite o vetor: ")))

acum = 0

for i in range(size(v)):
	if v[i]%3 == 0 :
		acum = acum + 1 
print(acum)

v2 = zeros(acum,dtype=int)

x = 0

for i in range(size(v)):
	if v[i]%3 == 0 : 
		v2[x]= i
		x = x + 1
	
print(v2)
	