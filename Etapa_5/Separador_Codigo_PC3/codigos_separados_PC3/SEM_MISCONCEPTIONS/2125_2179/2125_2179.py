from numpy import *

NParcial = array(eval(input("Notas das 3 atividades de um aluno: ")))

Prova = NParcial[0]
Trabalho = NParcial[1]
Seminario = NParcial[2]

NFinal=(Prova*3.0 + Trabalho*3.0 + Seminario*4.0)/10.0
print(round(NFinal, 2))

if(NFinal >= 5.0):
	msg= "aprovado"
	print(msg.upper())
else:
	msg = "reprovado"
	print(msg.upper())

