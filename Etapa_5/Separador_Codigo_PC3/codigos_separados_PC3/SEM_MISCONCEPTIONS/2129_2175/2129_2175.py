from numpy import *

vetornota = array(eval(input("Digite as notas: ")))

MFinal = (vetornota[0]*1.0 + vetornota[1]*2.0 + vetornota[2]*3.0 + vetornota[3]*4.0)/10.0
print(MFinal)
if (MFinal >= 5.0):
   print(round(MFinal, 2),"APROVADO")
else:
	print("REPROVADO")
	
	