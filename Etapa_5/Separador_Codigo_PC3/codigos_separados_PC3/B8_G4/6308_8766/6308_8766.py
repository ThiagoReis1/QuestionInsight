vet = input("Digite o tipo:")

A = 0
L = 0
P = 0

i = 0
total = 0

while i < len(vet):
	
	if vet[i] == "A":
		A = A + 1
		total = total + 16.75
	elif vet[i] == "L":
		L = L + 1
		total = total + 4.60
	elif vet[i] == "P":
		P = P + 1
		total = total + 2.85
	i = i + 1
print(round(total,2),A,L,P)