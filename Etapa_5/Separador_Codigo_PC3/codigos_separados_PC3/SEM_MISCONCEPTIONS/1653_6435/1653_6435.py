from numpy import*

paises = input("Paises: ").split(',')
cont = zeros(5, dtype=int)

for i in range(0, size(paises)):
	if (paises[i]) == 'AR':
		cont[0] += 1
	if (paises[i]) == 'BR':
		cont[1] += 1
	if (paises[i]) == 'CL':
		cont[2] += 1
	if (paises[i]) == 'CO':
		cont[3] += 1
	if (paises[i]) == 'UY':
		cont[4] += 1
print(max(cont))
print(cont)