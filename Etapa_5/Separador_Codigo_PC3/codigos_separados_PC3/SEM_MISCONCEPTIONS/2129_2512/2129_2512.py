from numpy import *
Nota = array(eval(input()))
MFinal = (Nota[0] * 1.0 + Nota[1] * 2.0 + Nota[2] * 3.0 + Nota[3] * 4.0) / 10.0
print(round(MFinal,2))
if(MFinal >= 5):
	t = "APROVADO"
else:
	t = "REPROVADO"
print(t)