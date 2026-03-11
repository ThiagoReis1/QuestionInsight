from numpy import*

ent = array(eval(input("")))
ent1 = array(eval(input("")))
vet2 = zeros(size(ent),dtype=float)
cont = 0

for i in range(size(ent)):
	vet2[i] = ent[i]+ent1[i]
	if(vet2[i] >= 12):
		cont += 1
print(vet2)
print(cont)