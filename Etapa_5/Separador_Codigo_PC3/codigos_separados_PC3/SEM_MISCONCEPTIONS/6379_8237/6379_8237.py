from numpy import*

notas = input("Digite uma nota:").upper().split(",")
vet = zeros(5,dtype=int)

for i in range(len(notas)):
	if notas[i] == "A":
		vet[0] = vet[0] + 1
	if notas[i] == "B":
		vet[1] = vet[1] + 1
	if notas[i] == "C":
		vet[2] = vet[2] + 1
	if notas[i] == "D":
		vet[3] = vet[3] + 1
	if notas[i] == "E":
		vet[4] = vet[4] + 1
print(vet)
		