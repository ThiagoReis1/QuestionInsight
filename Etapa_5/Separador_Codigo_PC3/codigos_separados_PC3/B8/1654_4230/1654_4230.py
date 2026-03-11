from numpy import*
string = input("Siglas: ").split(',')
vet = zeros(5,dtype=int)
for i in range(len(string)) :
	if string[i] == "AM" :
		vet[0] = vet[0] + 1
	elif string[i] == "PE" :
		vet[1] = vet[1] + 1
	elif string[i] == "MG" :
		vet[2] = vet[2] + 1
	elif string[i] == "SP" :
		vet[3] = vet[3] + 1
	elif string[i] == "RS" :
		vet[4] = vet[4] + 1
print(max(vet))
print(vet)