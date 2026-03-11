from numpy import*

vet = array(eval(input("vetores: ")))
vp = [2,2,6,1]

i = 0
cont = 0
while i < size(vet):
	if vet[i] == [0]:
		vp[cont] = vet[0] * vp[0]
	if vet[i] == [1]:
		vp[cont] = vet[1] * vp[1]
	if vet[i] == [2]:
		vp[cont] == vet[2] * vp[2]
	if vet[i] == [3]:
		vp[cont] == vet[3] * vp[3]
	i = i + 1
	
print(round(cont, 2))