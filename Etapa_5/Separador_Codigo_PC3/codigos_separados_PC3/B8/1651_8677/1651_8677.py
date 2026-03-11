from numpy import *
tpele = input("insira o tom de pele dos pacientes: ").split(',')

vet = zeros(6, dtype=int)

i = 0

while i < len(tpele):
	if tpele[i] == "MC":
		vet[0] += 1

	elif tpele[i] == "C":
		vet[1] += 1
	
	elif tpele[i] == "CM":
		vet[2] += 1
		
	elif tpele[i] == "EM":
		vet[3] += 1
	
	elif tpele[i] == "E":
		vet[4] += 1
		
	elif tpele[i] == "ME":
		vet[5] += 1
		
	i+=1
print(max(vet))
print(vet)