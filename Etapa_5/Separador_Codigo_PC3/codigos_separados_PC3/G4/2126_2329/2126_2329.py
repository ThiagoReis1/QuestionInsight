from numpy import *
vet = array(eval(input("vet:")))
mf = ((vet[0] * 5) + (vet[1] * 25/10) + (vet[2] * 25/10)) / 10
print(round(mf, 2))
if (mf >= 5):
	print("APROVADO")
else:
	print("REPROVADO")