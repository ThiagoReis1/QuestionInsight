from numpy import*
nota = array (eval(input("Digite suas notas:")))

MFinal = (sum(nota) - max(nota))/3.0
print(round(MFinal,2))

if (MFinal>=5.0):
	print ("APROVOU")
else:
	print ("REPROVOU")