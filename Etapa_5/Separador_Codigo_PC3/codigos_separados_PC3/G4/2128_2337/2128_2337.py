from numpy import*
vet = array(eval(input("notas: ")))

M = sum(vet) - max(vet)
MF = M/3
print(round(MF,2))
if(MF >= 50):
		x = "APROVADO"
else:
		x = "REPROVADO"
print(x)