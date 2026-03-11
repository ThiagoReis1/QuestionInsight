from numpy import*
vet=array(eval(input()))
NF=(vet[0]*2.0+vet[1]*3.0+vet[2]*5)/10.0
print(round(NF, 2))
if NF>=5:
	print("APROVADO")
else:
	print("REPROVADO")