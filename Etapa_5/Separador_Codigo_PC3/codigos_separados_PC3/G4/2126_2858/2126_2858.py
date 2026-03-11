from numpy import*

vet = array(eval(input("digite um vetor: ")))

m = (vet[0]* 5.0 + vet[1] *2.5 + vet[2] * 2.5)/10.0

print(round(m, 2))

if(m >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")