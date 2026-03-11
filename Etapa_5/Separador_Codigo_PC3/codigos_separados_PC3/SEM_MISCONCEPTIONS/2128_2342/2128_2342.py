from numpy import*
nota = array(eval(input("Digite uma nota :")))
MFinal = (sum(nota) - max(nota))/3.0
print(round(MFinal,2))


if(MFinal>=50.0):
	print("APROVADO")
else:
	print("REPROVADO")

