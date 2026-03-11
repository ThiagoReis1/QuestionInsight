from numpy import *
notas = array(eval(input("")))
NF = (notas[0]*2.0 + notas[1]*3.0 + notas[2]*5.0)/10.0
print(NF)
if(NF >= 5):
	print("APROVADO")
else:
	print("REPROVADO")

