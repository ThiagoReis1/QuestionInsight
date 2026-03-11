import numpy as np
ent = input()
ent = ent.split(",")

vet = ["AM","PE","MG","SP","RS"]
vet2 = [0,0,0,0,0]

for i in ent:
	vet2[vet.index(i)] = vet2[vet.index(i)] + 1

print(max(vet2))

saida = np.array(vet2, dtype = np.int)

print(saida)