from numpy import *

x = array(eval(input("Digite as notas : ")))



Mfinal = (x[0]*5+x[1]*2.5+x[2]*2.5)/10
print(round(Mfinal,2))

if Mfinal >=5:
	print("APROVADO")
else:
	print("REPROVADO")
	