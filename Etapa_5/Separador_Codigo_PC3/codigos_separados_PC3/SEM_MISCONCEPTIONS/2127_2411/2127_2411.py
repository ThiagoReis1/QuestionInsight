from numpy import*

nota = array(eval(input()))
mfinal = (sum(nota) - min(nota))/3
print(round(mfinal,2))
if(mfinal >= 50.0):
	print("APROVADO")	
else: 
	print("REPROVADO")
