from numpy import *
dano = array(eval(input("vetor de danos: ")))
i = 0
peso = 1
dano_total = 0
while (i < size(dano)):
	dano_total = dano_total + (dano[i] * peso)
	i = i + 1
	peso = peso + 1
print(dano_total)