from numpy import *

p = float (input ("Numero:"))
v = array (eval (input ("Vetor:")))
v1 = array (eval (input ("Vetor:")))

t = p / (p + 1)
n = 0

for i in range (size(v)):
	n = n + (abs (2 * v[i] + 3 * v1[i]) ** t)
n = n ** (1/t)
print (round (n, 7))
	