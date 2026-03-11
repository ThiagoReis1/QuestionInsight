from numpy import *
from numpy import *

p = float(input("Valor de P: "))
a = array(eval(input("Vetor 1: ")))
b = array(eval(input("Vetor 2: ")))

h = 0
n = 0
j = 0
t = ((p) / (p - 1))
ab = (2 * a + 3 * b)

for i in ab:
	n = n + (abs(i)) ** t
v = n ** (1/t)
print(round(v,3))

