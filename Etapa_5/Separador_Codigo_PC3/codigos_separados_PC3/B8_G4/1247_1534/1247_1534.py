#Suenne Renata Lima Fernandes
from numpy import *

v = array (eval (input ("Vetor:")))
v0 = zeros (2, dtype = int)

a = min(v)
b = max(v)

c = 0.75 * a + 0.25 * b
d = 0.25 * a + 0.75 * b

for i in range (size(v)):
	if (v[i] >= a and v[i] < c):
		v0[0] = v0[0] + 1
	elif (v[i] >= d and v[i] < b):
		v0[1] = v0[1] + 1
print (v0)
 