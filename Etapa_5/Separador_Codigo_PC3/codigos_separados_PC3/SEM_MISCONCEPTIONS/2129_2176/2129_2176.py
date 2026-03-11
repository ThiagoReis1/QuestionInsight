from numpy import *
vetor = array(eval(input("Digite as notas:")))
MFinal = ((vetor[0]*1.0)+(vetor[1]*2.0)+(vetor[2]*3.0)+(vetor[3]*4.0))/10.0
if(MFinal>5.0):
	print(round(MFinal,2))
	print("APROVADO")
else:
	print(round(MFinal,2))
	print("REPROVADO")