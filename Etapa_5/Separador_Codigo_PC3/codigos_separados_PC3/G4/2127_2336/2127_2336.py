from numpy import*
vet = array(eval(input()))

M = sum(vet) - min(vet)
MF = M/3
print(round(MF,2))
if MF >= 50.0:
	x = "APROVADO"
else:
	x = "REPROVADO"
print(x)


