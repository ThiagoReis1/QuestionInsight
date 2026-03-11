from numpy import*
from math import*

P = array(eval(input("Veotr P: ")))
Q = array(eval(input("Veotr Q: ")))

a = 0

for i in range(size(P)):
	a = a+(P[i] - Q[i])**2
	
D = sqrt(a)
s = 1/(1 + D)
print(round(D,4))
print(round(s,2))

