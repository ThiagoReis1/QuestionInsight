from numpy import*
from math import*
P = array(eval(input("Vetor P: ")))
Q = array(eval(input("Vetor Q: ")))

a = 0
for i in range(size(P)):
	a = a+(P[i] - Q[i])**2
D = sqrt(a)
print(round(D,4))