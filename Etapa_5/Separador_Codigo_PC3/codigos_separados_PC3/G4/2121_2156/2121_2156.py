from numpy import*
vet = array(eval(input("Notas parciais: ")))

soma = (vet[0]*5.0+vet[1]*3.0+vet[2]*2.0)/10
print(round(soma, 2))

if (soma >= 5):
	print("APROVADO")
else:
	print("REPROVADO")