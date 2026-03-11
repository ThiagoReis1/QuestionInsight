from numpy import *

v = array(eval(input("Entre: ")))

cont = 0 

for i in range(size(v)):
	if v[i] >= 2000:
		cont += 1
		
cont2= zeros(cont, dtype=int)
j=0
for i in range(size(v)):
	if v[i]>=2000:
		cont2[j]=i
		j=j+1

		
print(cont)
print(cont2)
		