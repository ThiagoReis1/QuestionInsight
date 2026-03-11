from numpy import *

n = array(eval(input("Digite o codigo: ")))
v = zeros(size(n),dtype=int)
for i in range(size(n)):
	v[i] = n[i] * 2
print(v)