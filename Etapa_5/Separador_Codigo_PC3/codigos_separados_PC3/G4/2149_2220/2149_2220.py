from numpy import*
v1=array(eval(input("Sas: ")))
v2=array(eval(input("Asas: ")))

vet= zeros(size(v1),dtype=float)
i = 0
for i in range(size(v2)):
	vet[i] = v1[i] + v2[i]
	if vet[i] >= 12:
		i = i + 1
print(vet)
print(i)