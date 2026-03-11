#Leticia Filardi - 21601147
#Avaliacao 6

from numpy import *

v = array (eval (input ("Vetor:")))
v0 = zeros (2, dtype = int)

a = min(v)
b = max(v)

c = 0.6 * a + 0.4 * b
d = 0.3 * a + 0.7 * b

for i in range (size(v)):
	if (v[i] >= c and v[i] < d):
		v0[0] = v0[0] + 1
	elif (v[i] >= d and v[i] < b):
		v0[1] = v0[1] + 1
print (v0)