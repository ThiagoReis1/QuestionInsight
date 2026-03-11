from numpy import *
entrada = input("Digite Países: ")
vet = entrada.split(',')
pais = ["CHN","JPN","KOR","MGL","THA"]
sai = zeros(size(pais), dtype = int)
for i in range(size(pais)):
	for j in range(size(vet)):
		if (vet[j] == pais[i]):
			sai[i] = sai[i] + 1
print(max(sai))
print (sai)