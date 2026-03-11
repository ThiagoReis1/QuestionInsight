from numpy import*
string = input(array(""))
vet = zeros(2,dtype=int)
for i in range(len(string)):
	if (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u") :
		vet[0] = vet[0] + 1
	else:
		vet[1] = vet[1] + 1
print(vet[0])
print(vet[1])