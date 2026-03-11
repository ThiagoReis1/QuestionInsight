from numpy import *
vet = input("Insira o vetor: ").upper().split(",")
t = 0
print(vet)
vett = zeros(vet, dtype=int)
for v in range(0,len(vett)):
	if vet[t] == 'C':
		t[0] = t[0] + 1
	elif vet[t] == 'D':
		t[1] = t[1] + 1
	elif vet[t] == 'V':
		t[2] = t[2] + 1
	else:
		t[3] = t[3] + 1
	t += 1
print(t)