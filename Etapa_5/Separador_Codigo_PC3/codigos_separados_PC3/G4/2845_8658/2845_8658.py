from numpy import *

n = array(eval(input(" ")))
n1 = zeros(size(n), dtype = int) 

for i in range(size(n)):
	if n[i] == 9:
		n1[i] = 0
	else: n1[i] = n[i] + 1

		
print(n1)