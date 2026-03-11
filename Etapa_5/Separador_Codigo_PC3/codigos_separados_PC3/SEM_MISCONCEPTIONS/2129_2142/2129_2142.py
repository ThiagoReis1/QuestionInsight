from numpy import *

notas = array(eval(input("Digite as notas: ")))

MFinal = (notas[0]*1.0 + notas[1]*2.0 + notas[2]*3.0 + notas[3]*4.0) / 10.0
print(round(MFinal, 2))

if(MFinal < 5):
	print("REPROVADO")
else:
	print("APROVADO")