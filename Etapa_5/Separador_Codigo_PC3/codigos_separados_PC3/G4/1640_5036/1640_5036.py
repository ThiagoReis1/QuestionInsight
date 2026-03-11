from numpy import * 

v = array(eval(input('valor dos indices: ')))
cont = 0
for x in v:
	if x % 2 != 0:
		cont += 1
vet = zeros(cont, dtype=int)
x = 0
for i in range(0, size(v)):
	if v[i] % 2 != 0:
		vet[x] = i
		x += 1
print(cont)

print(vet)