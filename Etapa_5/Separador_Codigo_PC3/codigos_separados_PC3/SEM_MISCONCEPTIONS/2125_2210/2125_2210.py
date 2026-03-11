from numpy import*

vet=eval(input("entre com a nota: "))

notafinal=(vet[0] * 3.0 + vet[1]* 3.0 + vet[2] * 4.0) / 10.0

print(round(notafinal,2))
if(notafinal>=5):
	print("APROVADO")
else:
	print("REPROVADO")

