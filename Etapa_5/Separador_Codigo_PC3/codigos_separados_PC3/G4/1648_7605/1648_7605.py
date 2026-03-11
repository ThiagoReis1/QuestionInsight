from numpy import *
v = array(eval(input("Aulas frequentadas: ")))
reprov = 0

for i in range(size(v)):
	if v[i] < 70:
		reprov = reprov + 1
		
x = zeros(reprov,dtype=int)	
j = 0
for i in range(size(v)):
	if v[i] < 70:
		x[j] = i
		j = j + 1
print(reprov)
print(x)
		
	
		
