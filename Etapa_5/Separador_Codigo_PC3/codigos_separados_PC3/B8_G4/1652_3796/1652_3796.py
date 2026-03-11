from numpy import*
s = input("string").split(",")
B = 0
PA = 0
PR = 0
A = 0
I = 0
vet = zeros(5, dtype = int)
for i in s:
	if i == "B":
		B += 1
	elif i == "PA":
		PA += 1
	elif i == "PR":
		PR += 1
	elif i == "A":
		A += 1
	elif i == "I":
		I += 1
vet[0]= B
vet[1] = PA
vet[2] = PR
vet[3] = A
vet[4] = I
print(max(vet))
print(vet)