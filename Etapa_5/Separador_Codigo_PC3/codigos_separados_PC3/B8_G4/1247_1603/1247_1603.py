
from numpy import *

v = array(eval(input("digite o vetor: ")))

A = min(v)
B = max(v)

C = (0.75*A) + (0.25*B)
D = (0.25*A) + (0.75*B)
	
vcont = zeros(2, dtype = int)

for j in range (size(v)):
	if(v[j] >= A and v[j] < C):
		vcont[0] = vcont[0] + 1
	elif (v[j] >= D and v[j] < B):
		vcont[1] = vcont[1] + 1
print(vcont)
			