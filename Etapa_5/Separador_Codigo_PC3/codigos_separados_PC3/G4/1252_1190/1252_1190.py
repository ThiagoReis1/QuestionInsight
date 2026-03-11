from numpy import *

v = array(eval(input()))

A=max(v)
B=min(v)
C=0.6 * A + 0.4 * B
D=0.3 * A + 0.7 * B

vcont = zeros(2, dtype=int)

for element in v:
	if (element >= A) and (element < C):
		vcont[0] = vcont[0] + 1
	else:
		vcont[1] = vcont[1] + 1
		
print(vcont)

print(A)
print(B)
print(C)
print(D)

