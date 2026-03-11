from numpy import*
Nota= array(eval(input("Nota:")))

MFinal = ((Nota[0] * 3.0) + (Nota[1] * 2.0) + (Nota[2] * 2.0) + (Nota[3] * 3.0)) / 10.0
print(round(MFinal,2))
if(MFinal >= 5):
	print("APROVADO")
else:
	print("REPROVADO")
