from numpy import *
p = str(input('paises: ').upper()).split(',')

cont = 0
ar = 0
br = 0
cl = 0 
co = 0
uy = 0
vet = zeros(5, dtype=int)
for x in p:
	if x == 'AR':
		vet[0] += 1
	elif x == 'BR':
		vet[1] += 1
	elif x == 'CL':
		vet[2] += 1
	elif x == 'CO':
		vet[3] += 1
	elif x == 'UY':
		vet[4] += 1

print(max(vet))
print(vet)