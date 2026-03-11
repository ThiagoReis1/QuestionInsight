from numpy import *
freqs = array(eval(input()))

repro = 0
vet_repro = []

for i in range(size(freqs)):
	if freqs[i] < 70:
		repro += 1
		vet_repro.append(i)

vet_repro = array(vet_repro)

print(repro)
print(vet_repro)