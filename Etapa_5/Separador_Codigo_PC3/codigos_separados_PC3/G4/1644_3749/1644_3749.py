from numpy import *

notas = array(eval(input("notas finais: ")))

i = 0

for x in notas:
	if (x < 5):
		i = i + 1
		
vet = zeros(i, dtype = int)

j = 0
n = 0

for n in range(size(notas)):
	if (notas[n] < 5):
		vet[n] = vet[n] + j
	j = j + 1
	

	
print(i)
print(vet)
	