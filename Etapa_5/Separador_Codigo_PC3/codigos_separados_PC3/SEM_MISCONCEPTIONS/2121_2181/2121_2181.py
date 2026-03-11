from numpy import *
vet_notas = array(eval(input("Digite as notas do aluno: ")))

Prova = vet_notas[0]
Seminario = vet_notas[1]
Trabalho = vet_notas[2]

Nota_Final = (Prova * 5.0 + Seminario * 3.0 + Trabalho * 2.0)/10.0

if	(Nota_Final >= 5.0):
	print(round(Nota_Final, 2))
	print("APROVADO")
else:
	print(round(Nota_Final, 2))
	print("REPROVADO")