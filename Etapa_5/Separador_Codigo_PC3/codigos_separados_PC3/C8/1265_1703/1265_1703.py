# Hanna Soares Rodrigues - 21650885

from numpy import*
from math import*

numero = float(input("Digite um numero: "))
x = array(eval(input("Vetor x: ")))
y = array(eval(input("Vetor y: ")))

expoente = numero/(numero-1)

for i in range(size(x)):
	vetor1 = x[i]*2
for j in range(size(y)):
	vetor2 = y[j]*3

vetor3 = vetor1 + vetor2
k = 0
v = zeros(size(x), dtype=float)
for k in range (size(vetor3)):
	v = v + (((vetor3[k])**expoente)**(1/expoente))
	k = k + 1

print(v)

