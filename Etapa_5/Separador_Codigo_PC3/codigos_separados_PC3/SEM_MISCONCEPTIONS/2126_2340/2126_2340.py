from numpy import*

notas = array(eval(input("Notas:")))

MFinal = (notas[0]*5.0+notas[1]*2.5+notas[2]*2.5)/10.0
print(round(MFinal,2))
if (MFinal >= 5.0):
	
	print("APROVADO")
else:
	print("REPROVADO")