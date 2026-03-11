from numpy import *
vet = input()
print(vet[2] + vet[3])
i  = 0
MC = 0
C  = 0
CM = 0
EM = 0
E  = 0
ME = 0
cor = ones(6, dtype=int)
cor = [0,0,0,0,0,0]
while(i < size(vet)):
	if(vet[i] + vet[i+1] == 'MC'):
		print("debug")
		MC = MC + 1
		cor[0] = MC
	if(vet[i] == 'C'):
		C = C + 1
		cor[1] = C
	if(vet[i] == 'CM'):
		CM = CM + 1
		cor[2] = CM
	if(vet[i] == 'EM'):
		EM = EM + 1
		cor[3] = EM
	if(vet[i] == 'E'):
		E = E + 1
		cor[4] = E
	if(vet[i] == 'ME'):
		ME = ME + 1
		cor[5] = ME
	i = i + 1
	
print(cor)