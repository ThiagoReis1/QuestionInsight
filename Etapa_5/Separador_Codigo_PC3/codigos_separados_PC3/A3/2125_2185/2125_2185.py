from numpy import *

vet_notas = array(eval(input("notas: ")))
Prova = vet_notas[0]
Seminario = vet_notas[1]
Trabalho = vet_notas[2]
Nota_Final = (vet_notas[0]* 3.0 + vet_notas[1] * 3.0 + vet_notas[2] * 4.0)/10.0
if(Nota_Final >= 5.0):
	print(round(Nota_Final, 2))
	print("APROVADO")
else:
	print(round(Nota_Final, 2))
	print("REPROVADO")
	