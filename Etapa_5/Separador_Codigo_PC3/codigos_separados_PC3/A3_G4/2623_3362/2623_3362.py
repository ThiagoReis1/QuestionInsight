from numpy import *
from numpy.linalg import *

a = array(eval(input("digite: ")))

lin = a.shape[1]
b= zeros(lin,dtype=int)

for i in range(size(a)):
	b[i]= sum(a[:,i])
ind = 0
for i in range(size(b)):
	if (min(b) == b)[i]:
		ind = i
print(ind)	
	
		