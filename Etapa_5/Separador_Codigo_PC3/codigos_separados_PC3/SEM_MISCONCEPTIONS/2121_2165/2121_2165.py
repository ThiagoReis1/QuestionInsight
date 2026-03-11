from numpy import*
notas = array(eval(input()))

Prova = notas[0]
Seminario = notas[1]
Trabalho = notas[2]

NotaFinal = (Prova*5.0 + Seminario*3.0 + Trabalho*2.0)/10
if(NotaFinal > 5.0):
	print(round(NotaFinal, 2))
	print("APROVADO")
else:
	print(round(NotaFinal, 2))
	print("REPROVADO")
