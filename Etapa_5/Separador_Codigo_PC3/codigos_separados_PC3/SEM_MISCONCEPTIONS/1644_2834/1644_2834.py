from numpy import *

v = array(eval(input("notas finais: ")))

soma = 0

for i in range(size(v)):
	if(v[i] < 5):
		soma = soma + 1

cont = zeros(soma, dtype = int)

j = 0

for i in range(size(v)):
	if v[i] < 5:
	cont[j] = v[i]
	j = j + 1

print(cont)