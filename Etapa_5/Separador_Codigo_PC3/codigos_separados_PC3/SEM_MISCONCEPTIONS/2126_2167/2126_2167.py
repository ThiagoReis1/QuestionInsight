from numpy import *
Nparcial = array(eval(input("Digite as 03 notas parciais: ")))
Nota0 = Nparcial[0]
Nota1 = Nparcial[1]
Nota2 = Nparcial[2]
MFinal = (Nota0 * 5.0 + Nota1 * 2.5 + Nota2 * 2.5) / 10.0

if(MFinal >= 5):
	mensagem = "APROVADO"
	print(round(MFinal, 2))
	print(mensagem)
else:
	mensagem = "REPROVADO"
	print(round(MFinal, 2))
	print(mensagem)
