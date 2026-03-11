from numpy import *
notas = array(eval(input("notas: ")))
a = max(notas)
MFinal = (notas[0] + notas[1] + notas [2] + notas[3] - a) / 3
print(round(MFinal,2))
if(MFinal >= 5):
	print("APROVOU")
else:
	print("REPROVOU")