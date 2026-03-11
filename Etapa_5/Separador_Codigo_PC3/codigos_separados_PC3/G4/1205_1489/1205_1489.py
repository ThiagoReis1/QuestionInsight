# Leticia Filardi - 21601147
# Avaliacao 5

from numpy import *

v = array (eval (input ("Distancia:")))

i = 0
k = 0
x = 8.95

while (i < size (v)):
	if (v [i] > x):
		k = k + 1
	i = i + 1
print (x)
print (k)