from numpy import *
from math import *
p = float(input("Digite um numero: "))
x = array(eval(input("Digite os elementos do vetor x: ")),dtype=float)
y = array(eval(input("Digite os elementos do vetor y: ")),dtype=float)
t = p / (p-1)
e1 = 0
for i in range(size(x)):
	e1 = e1 + abs(x[i] + y[i]) ** t
	z = (e1 ** (1 / t))
print(round(z,5))