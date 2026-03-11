from numpy import*
notas = array(eval(input("")))
mfinal = (notas[0]*5.0+notas[1]*2.5+notas[2]*2.5)/10
if(mfinal>=5.0):
	print(round(mfinal,2))
	print("APROVADO")
else:
	print(round(mfinal,2))
	print("REPROVADO")
