from numpy import*
vet = array(eval(input("vetor: ")))
nota0= vet[0]
nota1= vet[1]
nota2= vet[2]
nota3= vet[3]

mediaf = (nota0 * 1.0 + nota1 * 2.0 + nota2 * 3.0 + nota3 * 4.0) / 10.0
if(mediaf >= 5):
	print(round(mediaf,2))
	print("aprovado".upper())
else:
	print(round(mediaf,2))
	print("reprovado".upper())