from numpy import*
from math import*

p = float(input("Digite um valor p: "))
x = array(eval(input("Digite o vetor X: ")))
y = array(eval(input("Digite o vetor Y: ")))
t = p/(p-1)
raiz = 1/t
v = zeros(size(x), dtype = float)
v1 = 0
for k in range(size(x)):
	v[k] = x[k] + y[k]
for i in range(size(v)):
	v1 = v1 + abs(v[i]) ** t
print(round((v1 ** raiz), 5))
	