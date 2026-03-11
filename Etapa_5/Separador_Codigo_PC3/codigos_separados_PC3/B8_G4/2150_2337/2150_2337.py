from numpy import*

vet = array(eval(input()))
vet1 = zeros(4, dtype=int)

for i in range(size(vet)):
	if vet[i] == "BOTAFOGO":
		vet1[0] += 1
	elif vet[i] == "FLAMENGO":
		vet1[1] += 1
	elif vet[i] == "FLUMINENSE":
		vet1[2] += 1
	elif vet[i] == "VASCO":
		vet1[3] += 1
print(vet1)
		