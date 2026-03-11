from numpy import*

notas = array(eval(input(":")))
lin = shape(notas)[0]
vet = zeros(lin, dtype=float)

for i in range(lin):
	v = notas[i,:]
	vet[i] = max(v)
print(max(vet))