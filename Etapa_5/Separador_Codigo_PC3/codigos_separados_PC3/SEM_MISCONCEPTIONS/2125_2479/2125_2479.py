from numpy import *
vetor = array(eval(input("Notas: ")))
nf = ((vetor[0]*3) + (vetor[1]*3) + (vetor[2]*4))/10
if(nf >= 5):
	print(round(nf, 2))
	print("APROVADO")
	
else:
	print(round(nf, 2))
	print("REPROVADO")