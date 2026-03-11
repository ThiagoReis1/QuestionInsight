from numpy import *  

Nota = array(eval(input("Digite as notas do aluno : ")))

NF = ( Nota[0] * 2.0 + Nota[1] * 3.0 + Nota[2] * 5.0) / 10.0

print(round(NF , 2))

if(NF >= 5):
	print("APROVADO")
	
else :
	print("REPROVADO")
