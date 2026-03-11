import numpy as np
vet = np.array(eval(input()))
sai = np.zeros(len(vet),dtype = int)
for i in range(0, len(vet),1) :
	sai[i] = vet[i] * 2
print(sai)