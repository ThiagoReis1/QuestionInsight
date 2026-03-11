from numpy import *

notas = array(eval(input("Informe as 4 notas de um aluno: ")))
i = 0
nota = 0
while(i < size(notas)):
	nota = nota + (notas[i] * (i + 1))
	mfinal = nota / 10
	i = i + 1
	
print(round(mfinal, 2))

if(mfinal >= 5.0):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"
	
print(mensagem)