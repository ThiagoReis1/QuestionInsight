from numpy import *
notas = array(eval(input("")))
mf = (notas[0] + notas[1] + notas[3]) / 3
if mf > 50.0 :
	msg = "APROVADO"
else:
	msg = "REPROVADO"
print(round(mf, 2))
print(msg)