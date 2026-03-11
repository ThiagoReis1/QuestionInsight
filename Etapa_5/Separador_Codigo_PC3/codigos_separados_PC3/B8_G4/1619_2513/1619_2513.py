from numpy import*

vet1 = array(eval(input()))
vet2 = array(eval(input()))

i = 0
t = size(vet1)
custo = 0

while (i < t):
	if (vet2[i] == "MORNO"):
		custo = custo + (vet1[i] * 45)
	elif (vet2[i] == "QUENTE"):
		custo = custo + (vet1[i] * 90)
	elif (vet2[i] == "FRIO"):
		custo = custo + (vet1[i] * 0)
	i = i + 1
custo = custo * 0.005

print(round(custo,2))

