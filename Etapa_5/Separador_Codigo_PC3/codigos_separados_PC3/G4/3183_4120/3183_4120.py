from numpy import *

vet = array(eval(input("Digite os numeros de maneira decrescente: ")))
p = zeros(size(vet), dtype=int)

for i in range(size(vet)):
	if(i == 0):
		p[i] = vet[-1]
	else:
		p[i] = vet[i-2]

print(p)
