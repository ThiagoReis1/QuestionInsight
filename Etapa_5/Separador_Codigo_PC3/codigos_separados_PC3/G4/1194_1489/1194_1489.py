# Leticia Filardi - 21601147
# Avaliacao 5

from numpy import *

v = array (eval (input ("Temperatura:")))

i = 0
k = 0
x = -100

while (i < size (v)):
	if (v [i] > x):
		k = k + 1
	i = i + 1

v1 = array (zeros (k, dtype = float))

i = 0
k = 0
while (i < size (v)):
	if (v [i] > x):
		v1 [k] = v [i]
		k = k + 1
	i = i + 1
print (v1)		