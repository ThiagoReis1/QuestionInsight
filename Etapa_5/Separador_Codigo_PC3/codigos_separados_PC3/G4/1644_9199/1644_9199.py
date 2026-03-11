from numpy import *

v = array(eval(input("digite:")))
rep = 0

for i in range(size(v)):
	if v[i] < 5:
		rep += 1
print(rep)
		
vc = zeros(rep, dtype=int)		
j = 0

for i in range(size(v)):
	if v[i] < 5:
		vc[j] = v[i]
		j += 1
print(vc)		
	