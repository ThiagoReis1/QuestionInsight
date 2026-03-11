from numpy import*
vetor= array(eval(input("notas: ")))

nf=(vetor[0]*3 + vetor[1]*2 + vetor[2]*2 + vetor[3]*3)/(10)

if(nf >=5):
	print(round(nf, 2))
	print("APROVADO")
	
else:
	print(round(nf, 2))
	print("REPROVADO")
