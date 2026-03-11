from numpy import*

nota = array (eval (input ("")))

prova = nota [0]
Seminario = nota[1]
trabalho = nota [2]


NotaFinal = ((prova*5.0) + (Seminario*3.0) + (trabalho*2.0))/10.0
print (round (NotaFinal, 2))

if (NotaFinal >= 5.0):
	print ("APROVADO")
else:
	print ("REPROVADO")