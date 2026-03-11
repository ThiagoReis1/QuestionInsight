from numpy import*

vet = zeros(10,dtype=float)
c = 0
t = 0
for i in range(size(vet)):
	while c < 10:
		notas = float(input("notas: "))
		c += 1
	media = float(input("media: "))
	if notas > media:
		t += 1
		vet[i] = notas

print(vet)
		
