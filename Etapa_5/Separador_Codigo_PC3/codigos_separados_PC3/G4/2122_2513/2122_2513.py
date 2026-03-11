from numpy import*

vet = array(eval(input()))

mf = (vet[0] * 2.0 + vet[1] * 3 + vet [2]*5)/10
print(round(mf,2))

if mf > 5.0:
	print("APROVADO")
else:
	print("REPROVADO")