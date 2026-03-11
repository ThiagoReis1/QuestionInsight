from numpy import*
Notas = array(eval(input("")))

MFinal = (Notas[0]*1.0 + Notas[1]*2.0 + Notas[2]*3.0 + Notas[3]*4.0)/10.0

if MFinal >= 5.0:
	msg = "APROVADO"
else:
	msg = "REPROVADO"
print(round(MFinal, 2))	
print(msg)